from django.db import models

from edc_base.model.models import BaseUuidModel

from ..choices import FOLLOW_UP
from ..constants import CLOSED, OPEN, NEW

from .work_list import WorkList


class FollowUpList(BaseUuidModel):
    work_list = models.ForeignKey(WorkList)

    followup = models.CharField(
        max_length=50,
        choices=FOLLOW_UP
        )

    call_datetime = models.DateTimeField(
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
 
#     objects = CallListManager()

    class Meta:
        app_label = 'contact'
