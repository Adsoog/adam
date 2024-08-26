from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from resources.models import Resource, Hazard

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['resource','resource_type'] 

    def __init__(self, *args, **kwargs):
        super(ResourceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('resource', css_class='form-group col-md-12 mb-0'),
                Column('resource_type', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Guardar', css_class='btn btn-primary mt-2')
        )
        self.fields['resource'].widget.attrs.update({'placeholder': 'Descripción del Recurso', 'class': 'form-control'})
        self.fields['resource'].label = ''
        self.fields['resource_type'].widget.attrs.update({'class': 'form-control'})
        self.fields['resource_type'].label = ''
        
class HazardForm(forms.ModelForm):

    hazard = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Describa el peligro asociado aquí',
            'class': 'form-control'
        }),
        label='',
        required=False
    )

    risk_description = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Describa el riesgo asociado aquí',
            'class': 'form-control'
        }),
        label='',
        required=False
    )

    cause_description = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Describa la causa aquí',
            'class': 'form-control'
        }),
        label='',
        required=False
    )

    control_measures = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Describa las medidas de control aquí',
            'class': 'form-control'
        }),
        label='',
        required=False
    )

    class Meta:
        model = Hazard
        fields = ['resources', 'hazard', 'risk_description', 'cause_description', 'control_measures']

    def __init__(self, *args, **kwargs):
        super(HazardForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('hazard', css_class='form-group col-md-6 mb-0'),
                Column('resources', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('hazard_description', css_class='form-group col-md-6 mb-0'),
                Column('risk_description', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('cause_description', css_class='form-group col-md-6 mb-0'),
                Column('control_measures', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Guardar', css_class='btn btn-primary mt-2')
        )

        # Configurar atributos de los widgets y labels
        for field_name in self.fields:
            field = self.fields[field_name]
            field.widget.attrs.update({'class': 'form-control'})
            field.label = ''

class AssignResourceForm(forms.Form):
    resources = forms.ModelMultipleChoiceField(
        queryset=Resource.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Asignar Recursos:",
        required=False  # Optional selection
    )