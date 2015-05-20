from datetime import datetime

from django.db import models

from edc_base.model.models import BaseUuidModel

# from edc.audit.audit_trail import AuditTrail
# from edc.base.model.fields import OtherCharField
# from edc.core.crypto_fields.fields import EncryptedTextField
# from edc.base.model.validators import date_is_future
# from edc.choices import 
# from edc.constants import YES, NO, DEAD
# 
# 
# from ..managers import CallLogEntryManager, CallLogManager
# from ..validators import date_in_survey
# 
# from .subject_locator import SubjectLocator


class CallLog (BaseUuidModel):

    '''Maintain a log of calls for a particular participant'''

    subject_identifier = models.CharField(
        verbose_name="Subject Identifier",
        max_length=50,
        blank=True,
        db_index=True,
        unique=True,
    )

#     locator_information = EncryptedTextField(
#         help_text='This information has been imported from the previous locator. You may update as required.')
# 
#     contact_notes = EncryptedTextField(
#         null=True,
#         blank=True,
#         help_text='')

#     label = models.CharField(
#         max_length=25,
#         null=True,
#         editable=False,
#         help_text="from call list"
#         )

#     history = AuditTrail()

#     objects = CallLogManager()

#     def __unicode__(self):
#         return '{} {} {} ({} call)'.format(
#             self.household_member.first_name,
#             self.household_member.initials,
#             self.household_member.household_structure.survey.survey_name,
#             self.label)

#     def save(self, *args, **kwargs):
#         update_fields = kwargs.get('update_fields', [])
#         if not self.survey:
#             self.survey = Survey.objects.current_survey(datetime.today())
#         if 'locator_information' in update_fields or not self.locator_information:
#             try:
#                 self.locator_information = SubjectLocator.objects.previous(
#                     self.household_member).formatted_contact_information
#             except AttributeError as err_message:
#                 self.locator_information = str(err_message)
#         super(CallLog, self).save(*args, **kwargs)
# # 
#     def natural_key(self):
#         return self.household_member.natural_key() + (self.label, )
#     natural_key.dependencies = ['bcpp_household_member.household_member', ]

    class Meta:
        app_label = 'contact'
#         unique_together = ['household_member', 'label']


