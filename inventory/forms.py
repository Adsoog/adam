from django import forms
from .models import Equipos, EPPS, Transporte, Materiales, Consumibles, Alimentos, ManoDeObra, Herramientas, Misc, BaseInventario

class EquiposForm(forms.ModelForm):
    class Meta:
        model = Equipos
        fields = '__all__'

class EPPSForm(forms.ModelForm):
    class Meta:
        model = EPPS
        fields = '__all__'

class TransporteForm(forms.ModelForm):
    class Meta:
        model = Transporte
        fields = '__all__'

class MaterialesForm(forms.ModelForm):
    class Meta:
        model = Materiales
        fields = '__all__'

class ConsumiblesForm(forms.ModelForm):
    class Meta:
        model = Consumibles
        fields = '__all__'

class AlimentosForm(forms.ModelForm):
    class Meta:
        model = Alimentos
        fields = '__all__'

class ManoDeObraForm(forms.ModelForm):
    class Meta:
        model = ManoDeObra
        fields = '__all__'

class HerramientasForm(forms.ModelForm):
    class Meta:
        model = Herramientas
        fields = '__all__'

class MiscForm(forms.ModelForm):
    class Meta:
        model = Misc
        fields = '__all__'

class BaseInventarioForm(forms.ModelForm):
    class Meta:
        model = BaseInventario
        fields = '__all__'