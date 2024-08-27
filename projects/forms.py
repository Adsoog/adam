# projects/forms.py
from django import forms
from .models import Contractor, Client, Project

class ContractorForm(forms.ModelForm):
    class Meta:
        model = Contractor
        fields = '__all__'

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = '__all__'