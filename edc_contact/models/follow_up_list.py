from django.db import models

from edc_base.model.models import BaseUuidModel

try:
    from edc_sync.mixins import SyncMixin
except:
    SycnMixin = type('SyncMixin', (object, ), {})

from edc_contact import FOLLOW_UP
from edc_contact import CLOSED, OPEN, NEW
from edc_contact import FollowUpListManager

from edc_contact import WorkList


class FollowUpList(SyncMixin, BaseUuidModel):

    work_list = models.ForeignKey(WorkList)

    followup = models.CharField(
        max_length=50,
        choices=FOLLOW_UP
        )

    contact_datetime = models.DateTimeField(
        null=True,
        editable=False,
        help_text='last call datetime updated by call log entry',
        )

    attempts = models.IntegerField(
        default=0)

    coutcome = models.TextField(
        max_length=150,
        null=True,
        )

    status = models.CharField(
        max_length=15,
        choices=(
            (NEW, 'New'),
            (OPEN, 'Open'),
            (CLOSED, 'Closed'),
            ),
        default=NEW,
        )

#     history = AuditTrail()

    objects = FollowUpListManager()

    def natural_key(self):
        return self.subject_identifier

    class Meta:
        app_label = 'edc_contact'
