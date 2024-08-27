from decimal import Decimal
from django.db import models

class SalesOrder(models.Model):
    sapcode = models.CharField(max_length=50)
    project = models.CharField(max_length=255)
    detail = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return f"{self.sapcode} - {self.project} - {self.detail}"
    
class SalesOrderItem(models.Model):
    salesorder = models.ForeignKey(SalesOrder,on_delete=models.CASCADE)
    sapcode_item = models.CharField(max_length=50, null=True, default="")
    description_item = models.CharField(max_length=50, null=True, default="")
    amount_item = models.IntegerField(null=True, default=0)
    ordered_item = models.IntegerField(default=0)
    remaining_item = models.IntegerField(null=True, default=0)
    gross_price_tem = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    total_gross_item = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    remaining_gross_item = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=Decimal('0.00'))
    enviado = models.BooleanField(default=False)
    solicitar_nueva_orden = models.BooleanField(default=False)

class OrdenDeCompra(models.Model):  
    item_orden_venta = models.ForeignKey(SalesOrderItem,on_delete=models.CASCADE,)
    clase = models.CharField(max_length=50, default="")
    tipo_pago = models.CharField(max_length=50, default="")
    # Establece una relación ForeignKey con Proveedor
    proveedor = models.ForeignKey(
        Proveedor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    desc_articulo = models.CharField(max_length=50)
    detalle_articulo = models.CharField(max_length=150, default='')
    cantidad = models.IntegerField()
    codigo_sap = models.CharField(max_length=50)
    precio_actual = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    igv = models.DecimalField(max_digits=5, decimal_places=2, default=0)  # Porcentaje
    detraccion = models.DecimalField(
        max_digits=5, decimal_places=2, default=0
    )
    precio_total = models.DecimalField(
        max_digits=10, decimal_places=2, editable=False, default=0
    )
    cuotas = models.IntegerField(default=0)
    fecha_pago = models.DateField(null=True, blank=True, verbose_name="Fecha de Pago")
    fecha_pagada = models.DateField(null=True, blank=True, verbose_name="Fecha Pagada")
    monto_detraccion = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)
    
    # Aqui sera la orden de pago
    monto_pagado = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # Añade el campo comprobante_pago
    comprobante_pago = models.FileField(
        upload_to="comprobantes_pago/",  # Directorio donde se guardarán los archivos
        validators=[
            FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'jpeg', 'png'])
        ], 
        null=True,
        blank=True,
        verbose_name="Comprobante de Pago",
    )
    numero_movimiento_bancario = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        default='',  # Establece el valor predeterminado como cadena vacía
        verbose_name="Número de Movimiento Bancario"
    )
    banco_relacionado = models.ForeignKey(
        'extractos.Banco',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Banco Relacionado"
    )
    restante_rendir = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False, verbose_name="Restante por Rendir")
    encargado = models.CharField(max_length=20, verbose_name="Encargado", blank=True, null=True)
