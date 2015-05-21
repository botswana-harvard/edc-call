from django.contrib import admin

from edc_base.modeladmin.admin import BaseModelAdmin

# from ..actions import call_participant, update_call_list_action
from ..forms import WorkListForm, FollowUpListForm
from ..models import WorkList, FollowUpList


class WorkListAdmin(BaseModelAdmin):

    form = WorkListForm
    date_hierarchy = 'created'

    radio_fields = {
        'gender':admin.VERTICAL
        }

    list_display = (
        "subject_identifier",
        'first_name',
        'initials',
        'gender',
        'age_in_years',
        'label',
        'created',
        "consent_datetime",
        'hostname_created',
        'user_created',
        )
    list_filter = (
        'label',
        'created',
        'gender',
        'consent_datetime',
        'hostname_created',
        'user_created',
        )

    search_fields = ('subject_identifier',
                     'first_name',
                     'initials',
                     )

#     actions = [call_participant, update_call_list_action]

admin.site.register(WorkList, WorkListAdmin)


class FollowUpListAdmin(BaseModelAdmin):

    form = FollowUpListForm

    radio_fields = {
        'followup':admin.VERTICAL,
        'status':admin.VERTICAL
        }

admin.site.register(FollowUpList, FollowUpListAdmin)
