from edc_base.form.forms import BaseModelForm

from ..models import FollowUpList


class WorkListForm (BaseModelForm):

    class Meta:
        model = FollowUpList
