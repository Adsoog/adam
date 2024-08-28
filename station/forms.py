from django import forms
from .models import Station

class StationForm(forms.ModelForm):
    class Meta:
        model = Station
        fields = ['name', 'description']
