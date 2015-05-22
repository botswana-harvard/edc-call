from django import forms

from ..models import WorkList, FollowUpList


class WorkListForm (forms.ModelForm):

    class Meta:
        model = WorkList
        fields = '__all__'


class FollowUpListForm (forms.ModelForm):

    class Meta:
        model = FollowUpList
        fields = '__all__'
