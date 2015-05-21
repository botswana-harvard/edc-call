from datetime import date

from django.db import models

from edc.constants import DONE, IN_PROGRESS

from apps.bcpp_household_member.models import MemberAppointment, HouseholdMember
from apps.bcpp_survey.models import Survey

from ..models import HouseholdStructure, HouseholdWorkList, HouseholdLogEntry


def update_household_work_list(label=None, household_structure=None):
    HicEnrollment = models.get_model('bcpp_subject', 'HicEnrollment')
    SubjectConsent = models.get_model('bcpp_subject', 'SubjectConsent')
    current_survey = Survey.objects.current_survey()
    survey_datetime_start = current_survey.datetime_start
    created = 0
    updated = 0
    if household_structure:
        household_structures = [household_structure]
    else:
        household_structures = HouseholdStructure.objects.filter(
            survey=current_survey, enrolled=True, progress='Not Started')
    for household_structure in household_structures:
        try:
            appt_count = MemberAppointment.objects.filter(
                household_member__household_structure=household_structure,
                label=label).count()
            member_appointment = MemberAppointment.objects.filter(
                household_member__household_structure=household_structure, label=label).exclude(
                    appt_status__in=[DONE, IN_PROGRESS]).order_by('appt_date')[0]
            appt_date = member_appointment.appt_date
            status = 'scheduled'
        except IndexError:
            appt_date = date.today()
            status = 'unscheduled'
        if HicEnrollment.objects.filter(
                subject_visit__household_member__household_structure__household=household_structure.household,
                subject_visit__household_member__household_structure__survey__datetime_start__lt=survey_datetime_start,
                ).count() > 0:
            enrolled_type = 'hic'
        else:
            enrolled_type = 'bhs'
        try:
            log_attempts = HouseholdLogEntry.objects.filter(
                household_log__household_structure=household_structure).count()
            household_log_entry = HouseholdLogEntry.objects.filter(
                household_log__household_structure=household_structure).order_by('-report_datetime')[0]
            log_date = household_log_entry.report_datetime  # TODO: report_datetime is a date, not datetime!
            log_status = household_log_entry.household_status
        except IndexError:
            log_date = None
            log_status = None
        member_count = HouseholdMember.objects.filter(household_structure=household_structure).count()
        hic_count = HicEnrollment.objects.filter(
            subject_visit__household_member__household_structure__household=household_structure.household).count()
        bhs_count = SubjectConsent.objects.filter(
            household_member__household_structure__household=household_structure.household).count()
        try:
            household_work_list = HouseholdWorkList.objects.get(household_structure=household_structure, label=label)
            household_work_list.visit_date = appt_date
            household_work_list.status = status
            household_work_list.appt_count = appt_count
            household_work_list.enrolled_type = enrolled_type
            household_work_list.log_date = log_date
            household_work_list.log_status = log_status
            household_work_list.log_attempts = log_attempts
            household_work_list.members = member_count
            household_work_list.hic = hic_count
            household_work_list.bhs = bhs_count
            household_work_list.save()
            updated += 1
        except HouseholdWorkList.DoesNotExist:
            HouseholdWorkList.objects.create(
                household_structure=household_structure,
                survey=household_structure.survey,
                label=label,  # TODO:
                visit_date=appt_date,
                status=status,
                appt_count=appt_count,
                enrolled_type=enrolled_type,
                log_date=log_date,
                log_status=log_status,
                log_attempts=log_attempts,
                members=member_count,
                hic=hic_count,
                bhs=bhs_count,
                )
            created += 1
    return created, updated
