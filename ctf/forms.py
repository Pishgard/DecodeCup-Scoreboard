from django import forms
from .models import Submit


class SubmitForm(forms.ModelForm):
    STATUS_CHOICES = [
        (False, 'غلط'),
        (True, 'درست'),
    ]
    status = forms.ChoiceField(label='وضعیت پاسخ', choices=STATUS_CHOICES, initial=1,
                               widget=forms.Select())
    class Meta:
        model = Submit
        fields = ['team', 'level', 'team_broken', 'status', 'time']