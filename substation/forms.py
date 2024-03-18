from django import forms
from .models import Substation


class SubstationForm(forms.ModelForm):
    class Meta:

        model = Substation
        fields = ["city", "view", "number"]

