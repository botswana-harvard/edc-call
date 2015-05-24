from datetime import datetime

from django.test import TestCase

from ..models import CallLog, CallLogEntry, WorkList, FollowUpList


class CallLogModelTest(TestCase):
    def setUp(self):
        self.log = CallLog.objects.create(
            subject_identifier='987-098-9',
            locator_information='BHP, DMC',
            contact_notes='BHP Number',
            label='List label'
        )
        CallLogEntry.objects.create(
            call_log=self.log,
            contact_type='Direct edc_contact with participant',
            survival_status='Alive',
            call_datetime=datetime.today()
        )
        self.work_list = WorkList.objects.create(
            subject_identifier='987-098-9',
            first_name='Bella',
            initials='BB',
            gender='F',
            consent_datetime=datetime.today(),
        )
        FollowUpList.objects.create(
            work_list=self.work_list,
            followup='SMS',
            contact_datetime=datetime.today(),
            attempts=2,
        )

    def test_calllog_model_save(self):
        '''Test that model CallLog can be saved and queried'''
        log = CallLog.objects.get(subject_identifier='987-098-9')
        self.assertEqual(log.label, 'List label', 'Failed: Not Equal')
        log.locator_information = 'Call after 6pm'
        log.save()
        self.assertEqual(log.locator_information, 'Call after 6pm', 'Failed: Not Equal')

    def test_calllogentry_model_save(self):
        '''Test that model CallLogEntry can be saved and queried'''
        log_entry = CallLogEntry.objects.get(survival_status='Alive')
        self.assertEqual(log_entry.call_again, 'Yes', 'Failed: Not Equal')
        log_entry.survival_status = 'Dead'
        log_entry.save()
        self.assertEqual(log_entry.survival_status, 'Dead', 'Failed: Not Equal')

    def test_worklist_model_save(self):
        w_list = WorkList.objects.get(subject_identifier='987-098-9')
        self.assertEqual(w_list.first_name, 'Bella', 'Failed: not Equal')
        w_list.first_name = 'Bene'
        w_list.save()
        self.assertEqual(w_list.first_name, 'Bene', 'Failed: Not Equal')

    def test_followup_model_save(self):
        fu_list = FollowUpList.objects.get(followup='SMS')
        self.assertEqual(fu_list.followup, 'SMS', 'Failed: not Equal')
        fu_list.followup = 'Call'
        fu_list.save()
        self.assertEqual(fu_list.followup, 'Call', 'Failed: Not Equal')
