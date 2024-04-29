from django import forms
from .models import Switchgear


class SwitchgearForm(forms.ModelForm):
    class Meta:
        model = Switchgear
        fields = ["title"]

