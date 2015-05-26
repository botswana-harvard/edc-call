from dateutil.relativedelta import relativedelta

from django.core.urlresolvers import reverse
from django.db import models
from django_crypto_fields.fields import FirstnameField

from edc_constants.choices import GENDER_UNDETERMINED
from edc_base.model.models import BaseUuidModel
from edc_base.model.validators import (datetime_not_future,
                                       datetime_not_before_study_start)
try:
    from edc_sync.mixins import SyncMixin
except ImportError:
    SyncMixin = type('SyncMixin', (object, ), {})

from ..managers import WorkListManager


class WorkList(SyncMixin, BaseUuidModel):

    """A system model that helps track certain system values. """
    subject_identifier = models.CharField(
        max_length=25)

    first_name = FirstnameField(
        verbose_name='First name',
        editable=False,
    )

    initials = models.CharField(
        verbose_name='Initials',
        max_length=3,
        editable=False,
    )

    gender = models.CharField(
        verbose_name='Gender',
        max_length=1,
        choices=GENDER_UNDETERMINED,
        editable=False,
    )

    age_in_years = models.IntegerField(
        verbose_name=('Age in years'),
        null=True,
        editable=False,
    )

    consent_datetime = models.DateTimeField(
        verbose_name="Consent date and time",
        validators=[
            datetime_not_before_study_start,
            datetime_not_future, ],
        help_text=("From Subject Consent.")
    )

    label = models.CharField(
        max_length=25,
        null=True,
        help_text="label to group reasons for contact, e.g. preparation"
    )

    note = models.CharField("Note", max_length=250, blank=True)

    def age(self):
        return relativedelta(self.consent_datetime.date(), self.dob).years
    age.allow_tags = True

    objects = WorkListManager()
#
#     history = AuditTrail()

    def natural_key(self):
        return self.subject_identifier

    def follow_up_list(self):
        url = reverse('admin:contact_followuplist_changelist')
        return """<a href="{url}?q={q}" />followup list</a>""".format(
            url=url, q=self.work_list)
    follow_up_list.allow_tags = True

    class Meta:
        app_label = 'edc_contact'
