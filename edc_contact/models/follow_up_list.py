from django.db import models
from django.core.urlresolvers import reverse

from edc_base.model.models import BaseUuidModel
from edc_constants.constants import CLOSED, OPEN, NEW

try:
    from edc_sync.mixins import SyncMixin
except ImportError:
    SyncMixin = type('SyncMixin', (object, ), {})

from ..choices import FOLLOW_UP
# from ..managers import FollowUpListManager

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
            (CLOSED, 'Closed')),
        default=NEW,
    )

#     history = AuditTrail()

#    objects = FollowUpListManager()

    def call_list(self):
        url = reverse('admin:contact_worklist_changelist')
        return """<a href="{url}?q={q}" />worklist list</a>""".format(
            url=url, q=self.work_list.pk)
    call_list.allow_tags = True

    def natural_key(self):
        return self.subject_identifier

    class Meta:
        app_label = 'edc_contact'
