from edc_base.form.forms import BaseModelForm

from ..models import WorkList, FollowUpList


class WorkListForm (BaseModelForm):

    class Meta:
        model = WorkList


class FollowUpListForm (BaseModelForm):

    class Meta:
        model = FollowUpList
