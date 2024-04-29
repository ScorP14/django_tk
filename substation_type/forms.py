from django import forms

from substation_type.models import SubstationType


class SubstationTypeForm(forms.ModelForm):
    class Meta:
        model = SubstationType
        fields = ["title"]

