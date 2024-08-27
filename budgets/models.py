from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from projects.models import Project
from django.utils import timezone
from decimal import Decimal

from django.db import models
from django.utils import timezone

from decimal import Decimal

class Budget(models.Model):
    CURRENCY_CHOICES = [
        ('USD', 'Dólares'),
        ('PEN', 'Soles'),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='budgets', verbose_name="Proyecto")
    budget_name = models.CharField(max_length=100, default="", verbose_name="Presupuesto - Cotización")
    dias = models.PositiveIntegerField()
    total_soles_parcial = models.DecimalField(max_digits=12, decimal_places=2, default=0)  # Total parcial en soles
    total_dolares_parcial = models.DecimalField(max_digits=12, decimal_places=2, default=0)  # Total parcial en dólares
    total_soles_final = models.DecimalField(max_digits=12, decimal_places=2, default=0)  # Total final en soles
    total_dolares_final = models.DecimalField(max_digits=12, decimal_places=2, default=0)  # Total final en dólares
    tipo_cambio = models.DecimalField(max_digits=10, decimal_places=3, default=3.75)  # Tipo de cambio por defecto
    numero_cotizacion = models.CharField(max_length=10, blank=True)
    fecha = models.DateField(default=timezone.now)
    moneda = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='USD')
    impuesto = models.DecimalField(max_digits=5, decimal_places=2, default=18.00)
    tiempo_entrega = models.CharField(max_length=100, blank=True, null=True)
    tiempo_servicio = models.CharField(max_length=100, blank=True, null=True)
    facturacion = models.CharField(max_length=100, blank=True, null=True)
    tiempo_garantia = models.CharField(max_length=100, blank=True, null=True)
    no_incluye = models.TextField(blank=True, null=True)
    gastos_administrativos = models.DecimalField(max_digits=5, decimal_places=2, default=5.00)  # Porcentaje de gastos administrativos
    utilidad = models.DecimalField(max_digits=5, decimal_places=2, default=5.00)  # Porcentaje de utilidad
    total_utilidad = models.DecimalField(max_digits=12, decimal_places=2, default=0)  # Total de utilidad
    total_gastos_administrativos = models.DecimalField(max_digits=12, decimal_places=2, default=0)  # Total de gastos administrativos

    def __str__(self):
        return f'{self.project.nombre} - {self.dias} días - {self.numero_cotizacion}'

    def calcular_valor_total(self):
            # Sumar el precio de todos los items en soles (valor parcial)
        total_soles_parcial = Decimal(0)
        for item in self.items.all():
            total_soles_parcial += Decimal(item.precio_item_proyecto)
        
        self.total_soles_parcial = total_soles_parcial

        # Convertir el total parcial a dólares usando el tipo de cambio
        self.total_dolares_parcial = total_soles_parcial / Decimal(self.tipo_cambio)

        # Calcular gastos administrativos y utilidad
        self.total_gastos_administrativos = (total_soles_parcial * Decimal(self.gastos_administrativos)) / Decimal(100)
        self.total_utilidad = (total_soles_parcial * Decimal(self.utilidad)) / Decimal(100)

        # Sumar los gastos administrativos y la utilidad al total parcial para obtener el total final
        self.total_soles_final = total_soles_parcial + self.total_gastos_administrativos + self.total_utilidad

        # Convertir el total final a dólares usando el tipo de cambio
        self.total_dolares_final = self.total_soles_final / Decimal(self.tipo_cambio)

    def save(self, *args, **kwargs):
        if not self.numero_cotizacion:
            last_budget = Budget.objects.all().order_by('id').last()
            if last_budget and last_budget.numero_cotizacion.startswith('COT'):
                try:
                    last_number = int(last_budget.numero_cotizacion.split('COT')[-1])
                    self.numero_cotizacion = f'COT{str(last_number + 1).zfill(3)}'
                except ValueError:
                    self.numero_cotizacion = 'COT001'
            else:
                self.numero_cotizacion = 'COT001'

        # Guardar la instancia primero para obtener la PK
        super().save(*args, **kwargs)

        # Luego calcular el valor total en soles y dólares sin volver a guardar el presupuesto
        self.calcular_valor_total()

        
class BudgetItem(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name='items')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    inventario = GenericForeignKey('content_type', 'object_id')
    cantidad = models.PositiveIntegerField()
    real_price = models.FloatField(default=0)
    real_price_day = models.FloatField(default=0)
    unidad_medida = models.CharField(max_length=50, blank=True, default='')
    vida_util = models.PositiveIntegerField(default=365)
    precio_item_proyecto = models.FloatField(default=0)

    def __str__(self):
        return f'{self.inventario.descripcion} - {self.cantidad} {self.unidad_medida}'

    @property
    def precio_total_diario(self):
        return self.real_price_day * self.cantidad

    def save(self, *args, **kwargs):
        # Asigna los valores del inventario relacionado
        if not self.real_price:
            self.real_price = self.inventario.ultimo_precio_compra

        # Calcular el precio diario en base a la vida útil proporcionada
        self.real_price_day = self.real_price / self.vida_util

        # Calcular el precio del ítem para todo el proyecto
        if self.vida_util == 1:
            self.precio_item_proyecto = self.real_price * self.cantidad  # Se cuenta la cantidad
        else:
            self.precio_item_proyecto = self.precio_total_diario * self.budget.dias

        if not self.unidad_medida:
            self.unidad_medida = self.inventario.unidad_medida

        super().save(*args, **kwargs)

        # Calcular y actualizar el presupuesto después de guardar el ítem
        self.budget.calcular_valor_total()
        self.budget.save(update_fields=[
            'total_soles_parcial', 'total_dolares_parcial',
            'total_soles_final', 'total_dolares_final',
            'total_utilidad', 'total_gastos_administrativos'
        ])
