from django import forms
from .models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['substation', 'number_photo', 'date',
                  'switchgear', 'knot', 'number_cell',
                  't_env', 't_a', 't_b', 't_c',
                  'comment']
