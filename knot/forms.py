from django import forms
from .models import Knot


class KnotForm(forms.ModelForm):
    class Meta:
        model = Knot
        fields = ["title"]

