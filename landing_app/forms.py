# landing_app/forms.py

from django import forms
from .models import LandingData

class LandingDataForm(forms.ModelForm):
    class Meta:
        model = LandingData
        fields = ['background', 'logo', 'title', 'description']
