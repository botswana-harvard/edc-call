from datetime import datetime

from django.test import TestCase

from ..models import CallLog, CallLogEntry


class CallLogTest(TestCase):
    def setUp(self):
        self.log = CallLog.objects.create(subject_identifier = '987-098-9',
                               locator_information = 'BHP, DMC',
                               contact_notes = 'BHP Number',
                               label = 'List label')
        CallLogEntry.objects.create(call_log=self.log,
                                    contact_type='Direct contact with participant',
                                    survival_status='Alive',
                                    call_datetime=datetime.today()
                                   )

    def test_calllog_model_save(self):
        '''Test that model CallEntry can be saved and queried'''
        log = CallLog.objects.get(subject_identifier='987-098-9')
        self.assertEqual(log.label, 'List label', 'Failed: Not Equal')
        # Change data in saved model
        log.locator_information = 'Call after 6pm'
        # Re-save model
        log.save()
        self.assertEqual(log.locator_information, 'Call after 6pm', 'Failed: Not Equal')

    def test_calllogentry_model_save(self):
        '''Test that model CallLogEntry can be saved and queried'''
        log_entry = CallLogEntry.objects.get(call_log=self.log)
        self.assertEqual(log_entry.call_again, 'Yes', 'Failed: Not Equal')
        # Change data in saved model
        log_entry.survival_status = 'Dead'
        # Re-save model
        log_entry.save()
        # Assert that if survival stattus is dead then call again is no
        self.assertEqual(log_entry.survival_status, 'Dead', 'Failed: Not Equal')
