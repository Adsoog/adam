from django import forms
from inventory.models import Equipos, EPPS, Materiales, Transporte, Consumibles, Alimentos, ManoDeObra, Herramientas, Misc
from .models import Budget, BudgetItem
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Field, Submit
from crispy_forms.layout import Layout, Row, Column, Field, Submit, Div


class BudgetForm(forms.ModelForm):
    inventarios_equipos = forms.ModelMultipleChoiceField(
        queryset=Equipos.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'select2'}),
        required=False,
        label="Equipos"
    )
    inventarios_epps = forms.ModelMultipleChoiceField(
        queryset=EPPS.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'select2'}),
        required=False,
        label="EPPS"
    )
    inventarios_transporte = forms.ModelMultipleChoiceField(
        queryset=Transporte.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'select2'}),
        required=False,
        label="Transporte"
    )
    inventarios_materiales = forms.ModelMultipleChoiceField(
        queryset=Materiales.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'select2'}),
        required=False,
        label="Materiales"
    )
    inventarios_consumibles = forms.ModelMultipleChoiceField(
        queryset=Consumibles.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'select2'}),
        required=False,
        label="Consumibles"
    )
    inventarios_alimentos = forms.ModelMultipleChoiceField(
        queryset=Alimentos.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'select2'}),
        required=False,
        label="Alimentos"
    )
    inventarios_manodeobra = forms.ModelMultipleChoiceField(
        queryset=ManoDeObra.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'select2'}),
        required=False,
        label="Mano de Obra"
    )
    inventarios_herramientas = forms.ModelMultipleChoiceField(
        queryset=Herramientas.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'select2'}),
        required=False,
        label="Herramientas"
    )
    inventarios_misc = forms.ModelMultipleChoiceField(
        queryset=Misc.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'select2'}),
        required=False,
        label="Misceláneos"
    )

    FACTURACION_CHOICES = [
        ('50_50', '50% Adelantado y 50% Contraentrega'),
        ('al_credito', 'Al Crédito'),
        ('contado', 'Contado'),
    ]

    facturacion = forms.ChoiceField(
        choices=FACTURACION_CHOICES,
    )

    class Meta:
        model = Budget
        fields = [
            'project', 'budget_name', 'dias', 'fecha', 'moneda', 'tipo_cambio',
            'impuesto', 'tiempo_entrega', 'tiempo_servicio', 'facturacion', 
            'tiempo_garantia', 'no_incluye'
        ]
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'no_incluye': forms.Textarea(attrs={'placeholder': 'Items o servicios no incluidos en el servicio'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'project',
            'budget_name',
            'dias',
            'fecha',
            'moneda',
            'tipo_cambio',
            'impuesto',
            'tiempo_entrega',
            'tiempo_servicio',
            'facturacion',
            'tiempo_garantia',
            'no_incluye',
            'inventarios_equipos',
            'inventarios_epps',
            'inventarios_transporte',
            'inventarios_materiales',
            'inventarios_consumibles',
            'inventarios_alimentos',
            'inventarios_manodeobra',
            'inventarios_herramientas',
            'inventarios_misc',
            Submit('submit', 'Guardar')
        )


class BudgetItemQuantityForm(forms.ModelForm):
    VIDA_UTIL_CHOICES = [
        (1, 'Se quedará'),
        (14, '2 semanas'),  # 14 días
        (30, '1 mes'),  # 30 días
        (90, '3 meses'),  # 90 días
        (180, '6 meses'),  # 180 días
        (365, '1 año'),  # 365 días
        (730, '2 años'),  # 730 días
        (1095, '3 años'),  # 1095 días
        (1460, '4 años'),  # 1460 días
        (1825, '5 años'),  # 1825 días
    ]

    vida_util = forms.ChoiceField(choices=VIDA_UTIL_CHOICES, label="Vida Útil", initial=365)

    class Meta:
        model = BudgetItem
        fields = ['cantidad', 'real_price', 'real_price_day', 'unidad_medida', 'vida_util']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Configurar campos adicionales
        self.fields['real_price_day'].disabled = True  # Campo solo de lectura
        self.fields['unidad_medida'].disabled = True  # Campo solo de lectura

        # Convertir el valor de vida_util a días para que coincida con las opciones
        if self.instance.vida_util:
            self.fields['vida_util'].initial = self.instance.vida_util