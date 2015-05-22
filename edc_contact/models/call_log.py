from django_crypto_fields.fields import EncryptedTextField
from django.db import models

from edc_base.model.models import BaseUuidModel

from ..manangers import CallLogManager

try:
    from edc_sync.mixins import SyncMixin
except ImportError:
    SyncMixin = type('SyncMixin', (object, ), {})


class CallLog (SyncMixin, BaseUuidModel):

    '''Maintain a log of calls for a particular participant'''

    _subject_identifier = models.CharField(
        verbose_name="Subject Identifier",
        max_length=50,
        blank=True,
        db_index=True,
        unique=True,
    )

    locator_information = EncryptedTextField(
        help_text='This information has been imported from the previous locator. You may update as required.')

    contact_notes = EncryptedTextField(
        null=True,
        blank=True,
        help_text='')

    label = models.CharField(
        max_length=25,
        null=True,
        editable=False,
        help_text="from followup list"
        )

#     history = AuditTrail()

    @property
    def subject_identifier(self):
        return self._subjectidentifier

    @subject_identifier.setter
    def subject_identifier(self, value):
        self._subject_identifier=value

    objects = CallLogManager()

    def natural_key(self):
        return self.subject_identifier

    class Meta:
        app_label = 'contact'
