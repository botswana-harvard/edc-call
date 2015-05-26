from django.forms import ModelForm, ValidationError

from edc_constants.constants import ALIVE, DEAD, NO, YES, UNKNOWN

from ..models import CallLogEntry, CallLog


class CallLogForm (ModelForm):

    class Meta:
        model = CallLog
        fields = '__all__'


class CallLogEntryForm(ModelForm):

    def clean(self):
        cleaned_data = self.cleaned_data

        self.validate_not_alive(cleaned_data)
        self.validate_scheduled_appt(cleaned_data)

        if cleaned_data.get('contact_type') != 'direct' and cleaned_data.get('appt_date'):
            raise ValidationError(
                'You may may only schedule an appointment if contact is '
                'with the participant. Got contact_type=\'{}\''.format(
                    cleaned_data.get('contact_type')))

        self.validate_deceased(cleaned_data)
        self.validate_no_contact(cleaned_data)

        return self.cleaned_data

    def validate_not_alive(self, cleaned_data):
        if cleaned_data.get('survival_status') == DEAD and cleaned_data.get('appt_date'):
            raise ValidationError(
                'You may not schedule an appointment for a participant who is deceased. '
                'Got survival status = Dead.')

        if cleaned_data.get('survival_status') == DEAD and cleaned_data.get('appt') == YES:
            raise ValidationError(
                'Subject is willing to schedule an appointment but got '
                'survival status = Dead. Please correct.')

        if cleaned_data.get('survival_status') != ALIVE and cleaned_data.get('contact_type') == 'direct':
            raise ValidationError(
                'You indicate direct contact with the participant but '
                'survival status suggests otherwise. Got survival_status={}'.format(
                    cleaned_data.get('survival_status')))

    def validate_scheduled_appt(self, cleaned_data):
        if cleaned_data.get('appt') == NO and cleaned_data.get('appt_date'):
            raise ValidationError(
                'You may not schedule an appointment for a participant who is not willing '
                'to schedule an appointment.')

        if cleaned_data.get('appt') == YES and not cleaned_data.get('appt_date'):
            raise ValidationError(
                'Subject is willing to schedule an appointment. '
                'Please indicate the appointment date.')

        if cleaned_data.get('available') == NO and cleaned_data.get('appt_date'):
            raise ValidationError(
                'You may not schedule an appointment for a participant who is not available ')

    def validate_deceased(self, cleaned_data):
        if cleaned_data.get('survival_status') == DEAD:
            for item, value in cleaned_data.iteritems():
                if value and item not in [
                        'id', 'call_log', 'call_datetime', 'contact_type', 'survival_status',
                        'invalid_numbers', 'call_again']:
                    raise ValidationError(
                        '{} should be left blank. Got \'{}\' when survival status=Dead'.format(item, value))
            if self.cleaned_data.get('call_again') != NO:
                raise ValidationError(
                    'Indicate NOT to call participant again. Got survival_status=\'Dead\'')

    def validate_no_contact(self, cleaned_data):
        if cleaned_data.get('contact_type') == 'no_contact':
            for item, value in cleaned_data.iteritems():
                if value and item not in [
                        'id', 'call_log', 'call_datetime', 'contact_type', 'survival_status',
                        'invalid_numbers', 'call_again']:
                    raise ValidationError(
                        '{} should be left blank. Got \'{}\' when contact_type=\'No contact made\''.format(item, value))
            if self.cleaned_data.get('call_again') != YES and self.cleaned_data.get('survival_status') != DEAD:
                raise ValidationError(
                    'Indicate to call participant again. Got contact_type=\'No contact made\'')
            if self.cleaned_data.get('survival_status') != UNKNOWN:
                raise ValidationError(
                    'Expected survival status to be unknown.'
                    'Got contact_type=\'No contact made\'')

    class Meta:
        model = CallLogEntry
        fields = '__all__'
