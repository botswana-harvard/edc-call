from django.contrib import admin

from ..forms import CallLogForm, CallLogEntryForm
from ..models import CallLog, CallLogEntry


class CallLogEntryAdminInline(admin.StackedInline):
    instructions = [
        'Please read out instrauctions to participant.']

    form = CallLogEntryForm
    model = CallLogEntry
    max_num = 3
    extra = 0

    radio_fields = {
        "contact_type": admin.VERTICAL,
        "survival_status": admin.VERTICAL,
        "update_locator": admin.VERTICAL,
        "available": admin.VERTICAL,
        "time_of_week": admin.VERTICAL,
        "time_of_day": admin.VERTICAL,
        "appt": admin.VERTICAL,
        "appt_grading": admin.VERTICAL,
        "appt_location": admin.VERTICAL,
        "call_again": admin.VERTICAL,
    }


class CallLogAdmin(admin.ModelAdmin):

    instructions = [
        '<h5>Please read out instructions to participant:</h5>']

    form = CallLogForm

    fields = ('locator_information', 'contact_notes')

    inlines = [CallLogEntryAdminInline, ]

admin.site.register(CallLog, CallLogAdmin)


class CallLogEntryAdmin(admin.ModelAdmin):

    date_hierarchy = 'appt_date'
    instructions = [
        'Please read out to instaructions participant.']

    form = CallLogEntryForm

    radio_fields = {
        "contact_type": admin.VERTICAL,
        "survival_status": admin.VERTICAL,
        "update_locator": admin.VERTICAL,
        "available": admin.VERTICAL,
        "time_of_week": admin.VERTICAL,
        "time_of_day": admin.VERTICAL,
        "appt": admin.VERTICAL,
        "appt_grading": admin.VERTICAL,
        "appt_location": admin.VERTICAL,
        "call_again": admin.VERTICAL,
    }

    list_display = (
        'call_log',
        'call_datetime',
        'appt',
        'appt_date',
        'call_again',
    )

    list_filter = (
        'call_datetime',
        'appt',
        'appt_date',
        'call_again',
        'created',
        'modified',
        'hostname_created',
        'hostname_modified',
    )

    search_fields = (
        'subject_identifier',
        'first_name',
        'id'
    )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "call_log":
            kwargs["queryset"] = CallLog.objects.filter(id__exact=request.GET.get('call_log', 0))
        return super(CallLogEntryAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(CallLogEntry, CallLogEntryAdmin)
