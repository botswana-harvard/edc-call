from edc_base.form.forms import BaseModelForm

from ..models import FollowUpList


class FollowUpListForm (BaseModelForm):

    class Meta:
        model = FollowUpList
