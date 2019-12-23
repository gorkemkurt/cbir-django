from django import forms
from .models import *


class DestImageForm(forms.ModelForm):
    class Meta:
        model = DestImage
        fields = ['name', 'dest_image', 'feature_extraction_method']

