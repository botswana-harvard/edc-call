from django.db import models
from django.core.validators import RegexValidator

from edc_base.model.models import BaseUuidModel
from edc_base.model.validators import date_is_future
from edc_constants.choices import YES_NO, YES_NO_UNKNOWN, ALIVE_DEAD_UNKNOWN, TIME_OF_WEEK, TIME_OF_DAY
from edc_constants.constants import YES, NO, DEAD

try:
    from edc_sync.mixins import SyncMixin
except ImportError:
    SyncMixin = type('SyncMixin', (object, ), {})

from ..choices import CONTACT_TYPE, APPT_GRADING, APPT_LOCATIONS
from ..managers import CallLogEntryManager

from .call_log import CallLog


class CallLogEntry (SyncMixin, BaseUuidModel):

    '''Log a call made for a participant'''

    call_log = models.ForeignKey(CallLog)

    call_datetime = models.DateTimeField()

    invalid_numbers = models.CharField(
        verbose_name=('Indicate any invalid numbers dialed from the'
                      'locator information above?'),
        max_length=50,
        validators=[RegexValidator(
            regex=r'^[0-9]{7,8}(,[0-9]{7,8})*$',
            message=('Only enter contact numbers separated by commas.'
                     'No spaces and no trailing comma.')), ],
        null=True,
        blank=True,
        help_text='Separate by comma (,).'
    )

    contact_type = models.CharField(
        max_length=15,
        choices=CONTACT_TYPE,
        help_text='If no contact made. STOP. Save form.'
    )

    survival_status = models.CharField(
        verbose_name='Survival status of the participant',
        max_length=10,
        choices=ALIVE_DEAD_UNKNOWN,
        help_text=""
    )

    update_locator = models.CharField(
        max_length=7,
        verbose_name='Has the locator information changed',
        choices=YES_NO_UNKNOWN,
        null=True,
        blank=True,
        help_text=('If YES, please enter the changed information '
                   'in the box above entitled (2) Locator information')
    )

    available = models.CharField(
        max_length=7,
        verbose_name='Will the participant be available during the survey',
        choices=YES_NO_UNKNOWN,
        null=True,
        blank=True,
        help_text=""
    )

    time_of_week = models.CharField(
        verbose_name='Time of week when participant will be available',
        max_length=25,
        choices=TIME_OF_WEEK,
        blank=True,
        null=True,
        help_text=""
    )

    time_of_day = models.CharField(
        verbose_name='Time of day when participant will be available',
        max_length=25,
        choices=TIME_OF_DAY,
        blank=True,
        null=True,
        help_text=""
    )

    appt = models.CharField(
        verbose_name='Is the participant willing to schedule an appointment',
        max_length=7,
        choices=YES_NO_UNKNOWN,
        null=True,
        blank=True,
        help_text=""
    )

    appt_date = models.DateField(
        verbose_name="Appointment Date",
        validators=[date_is_future],
        null=True,
        blank=True,
        help_text="This can only come from the participant."
    )

    appt_grading = models.CharField(
        verbose_name='Is this appointment...',
        max_length=25,
        choices=APPT_GRADING,
        null=True,
        blank=True,
        help_text=""
    )

    appt_location = models.CharField(
        verbose_name='Appointment location',
        max_length=50,
        choices=APPT_LOCATIONS,
        null=True,
        blank=True,
        help_text=""
    )

    appt_location_other = models.CharField(
        verbose_name='Appointment location',
        max_length=50,
        null=True,
        blank=True,
        help_text=""
    )

    call_again = models.CharField(
        verbose_name='Call the participant again?',
        max_length=10,
        choices=YES_NO,
        default=YES,
        help_text=''
    )

#     history = AuditTrail()

    objects = CallLogEntryManager()

    def save(self, *args, **kwargs):
        if self.survival_status == DEAD:
            self.call_again = NO
        super(CallLogEntry, self).save(*args, **kwargs)

    def natural_key(self):
        return self.call_log.natural_key() + (self.call_datetime, )

    class Meta:
        app_label = 'edc_contact'
        unique_together = ['call_log', 'call_datetime']
