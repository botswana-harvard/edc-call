from django.contrib import admin

from edc.base.modeladmin.admin import BaseModelAdmin, BaseStackedInline

from apps.bcpp_household_member.models import HouseholdMember

from ..forms import CallLogForm, CallLogEntryForm
from ..models import CallLog, CallLogEntry


class CallLogEntryAdminInline(BaseStackedInline):
    instructions = [
        'Please read out to participant. "We hope you have been well since our visit last year. '
        'As a member of this study, it is time for your annual revisit in which we will ask you '
        'some questions and perform some tests."',
        'Please read out to contact other than participant. (Note: You may NOT disclose that the '
        'participant is a member of the Ya Tsie study). "We would like to contact a participant '
        '(give participant name) who gave us this number as a means to contact them. Do you know '
        'how we can contact this person directly? This may be a phone number or a physical address.']

    form = CallLogEntryForm
    model = CallLogEntry
    max_num = 3
    extra = 1

    fields = (
        'call_datetime',
        'invalid_numbers',
        'contact_type',
        'survival_status',
        'update_locator',
        'moved_community',
        'new_community',
        "moved_household",
        'available',
        'time_of_week',
        'time_of_day',
        'appt',
        'appt_date',
        'appt_grading',
        'appt_location',
        'appt_location_other',
        'call_again',
        )

    radio_fields = {
        "contact_type": admin.VERTICAL,
        "survival_status": admin.VERTICAL,
        "update_locator": admin.VERTICAL,
        "moved_community": admin.VERTICAL,
        "moved_household": admin.VERTICAL,
        "available": admin.VERTICAL,
        "time_of_week": admin.VERTICAL,
        "time_of_day": admin.VERTICAL,
        "appt": admin.VERTICAL,
        "appt_grading": admin.VERTICAL,
        "appt_location": admin.VERTICAL,
        "call_again": admin.VERTICAL,
        }


class CallLogAdmin(BaseModelAdmin):

    instructions = [
        '<h5>Please read out to participant:</h5> "We hope you have been well since our visit last year. '
        'As a member of this study, it is time for your annual revisit in which we will ask you '
        'some questions and perform some tests."',
        '<h5>Please read out to contact other than participant:</h5> (<B>IMPORTANT:</B> You may NOT disclose that the '
        'participant is a member of the Ya Tsie study).<BR>"We would like to contact a participant '
        '(give participant name) who gave us this number as a means to contact them. Do you know '
        'how we can contact this person directly? This may be a phone number or a physical address.']

    form = CallLogForm

    fields = ("household_member", 'locator_information', 'contact_notes')

    inlines = [CallLogEntryAdminInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "household_member":
            kwargs["queryset"] = HouseholdMember.objects.filter(id__exact=request.GET.get('household_member', 0))
        return super(CallLogAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(CallLog, CallLogAdmin)


class CallLogEntryAdmin(BaseModelAdmin):

    date_hierarchy = 'appt_date'
    instructions = [
        'Please read out to participant. "We hope you have been well since our visit last year. '
        'As a member of this study, it is time for your annual revisit in which we will ask you '
        'some questions and perform some tests."',
        'Please read out to contact other than participant. (Note: You may NOT disclose that the '
        'participant is a member of the Ya Tsie study). "We would like to contact a participant '
        '(give participant name) who gave us this number as a means to contact them. Do you know '
        'how we can contact this person directly? This may be a phone number or a physical address.']

    form = CallLogEntryForm
    fields = (
        'call_log',
        'call_datetime',
        'invalid_numbers',
        'contact_type',
        'survival_status',
        'update_locator',
        'moved_community',
        'new_community',
        "moved_household",
        'available',
        'time_of_week',
        'time_of_day',
        'appt',
        'appt_date',
        'appt_grading',
        'appt_location',
        'appt_location_other',
        'call_again',
        )

    radio_fields = {
        "contact_type": admin.VERTICAL,
        "survival_status": admin.VERTICAL,
        "update_locator": admin.VERTICAL,
        "moved_community": admin.VERTICAL,
        "moved_household": admin.VERTICAL,
        "available": admin.VERTICAL,
        "time_of_week": admin.VERTICAL,
        "time_of_day": admin.VERTICAL,
        "appt": admin.VERTICAL,
        "appt_grading": admin.VERTICAL,
        "appt_location": admin.VERTICAL,
        "call_again": admin.VERTICAL,
        }

    list_display = (
        'call_log',
        'call_datetime',
        'appt',
        'appt_date',
        'call_again',
    )

    list_filter = (
        'call_datetime',
        'appt',
        'appt_date',
        'call_again',
        'created',
        'modified',
        'hostname_created',
        'hostname_modified',
    )

    search_fields = ('call_log__household_member__registered_subject__subject_identifier', 'call_log__household_member__first_name', 'id')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "call_log":
            kwargs["queryset"] = CallLog.objects.filter(id__exact=request.GET.get('call_log', 0))
        return super(CallLogEntryAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(CallLogEntry, CallLogEntryAdmin)
