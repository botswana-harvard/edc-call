from django import forms

from ..models import WorkList, FollowUpList


class WorkListForm (forms.ModelForm):

    class Meta:
        model = WorkList


class FollowUpListForm (forms.ModelForm):

    class Meta:
        model = FollowUpList
