from edc_base.form.forms import BaseModelForm

from ..models import WorkListForm, FollowUpListForm


class WorkListForm (BaseModelForm):

    class Meta:
        model = WorkListForm


class FollowUpListForm (BaseModelForm):

    class Meta:
        model = FollowUpListForm
