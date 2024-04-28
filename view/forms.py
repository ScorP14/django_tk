from django import forms
from .models import View


class ViewForm(forms.ModelForm):
    class Meta:
        model = View
        fields = ["title"]
