from django.db import models

from edc_base.model.models import BaseUuidModel

try:
    from edc_sync.mixins import SyncMixin
except:
    SycnMixin = type('SyncMixin', (object, ), {})

from ..choices import FOLLOW_UP
from ..constants import CLOSED, OPEN, NEW
from ..manangers import FollowUpListManager

from .work_list import WorkList


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
        app_label = 'contact'
