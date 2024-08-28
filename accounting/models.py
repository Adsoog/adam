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
    price_item = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    total_price_item = models.DecimalField(max_digits=10, decimal_places=2, null=True)

class PurchaseOrderItem(models.Model):  
    sales_order_item     = models.ForeignKey(SalesOrderItem,on_delete=models.CASCADE,)
    purchase_class = models.CharField(max_length=50, default="")
    purchase_type = models.CharField(max_length=50, default="")
    purchase_supplier = models.ForeignKey(Proveedor,on_delete=models.SET_NULL,null=True,blank=True,)
    purchase_description = models.CharField(max_length=50)
    purchase_detail     = models.CharField(max_length=150, default='')
    purchase_amount = models.IntegerField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    purchase_total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False, default=0)
    purchase_requested_date = models.DateField(null=True, blank=True, verbose_name="Fecha Solicitada")
    purchase_paid_date = models.DateField(null=True, blank=True, verbose_name="Fecha Pagada")
    purchase_date = models.DateField(null=True, blank=True, verbose_name="Fecha de Pago")
    purchase_amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    purchase_proof = models.FileField(upload_to="comprobantes_pago/",validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'jpeg', 'png'])], null=True,blank=True, verbose_name="Comprobante de Pago",)
    purchase_number = models.CharField( max_length=255, null=True, blank=True, default='',)
    purchase_bank = models.ForeignKey('extractos.Banco', on_delete=models.SET_NULL,null=True,blank=True,verbose_name="Banco Relacionado" )
    purchase_yield = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False, verbose_name="Restante por Rendir")
    purchase_supervisor = models.CharField(max_length=20, verbose_name="Encargado", blank=True, null=True)

class CollectionOrderItem(models.Model):  
    sales_order_item     = models.ForeignKey(SalesOrderItem,on_delete=models.CASCADE,)
    serie_correlativo = models.CharField(max_length=100, verbose_name="Serie y Correlativo", null=True, blank=True)
    collection_date = models.DateField(verbose_name="Fecha de Emisión", null=True, blank=True)
    collection_client = models.CharField(max_length=255, verbose_name="Cliente", null=True, blank=True)
    collection_client_ruc = models.CharField(max_length=11, verbose_name="RUC Cliente", null=True, blank=True)
    collection_tipo_moneda = models.CharField(max_length=20, verbose_name="Tipo de Moneda", null=True, blank=True)
    collection_description = models.TextField(verbose_name="Descripción", null=True, blank=True)
    collection_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Importe Total", null=True, blank=True)
    collection_detraction = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Detracción", null=True, blank=True)
    collection_net_amunt = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Monto Neto a Cobrar", null=True, blank=True)
    collection_quotas = models.IntegerField(verbose_name="Total de Cuotas", null=True, blank=True)
    collection_expiration_date = models.DateField(verbose_name="Fecha de Vencimiento", null=True, blank=True)
    collection_payment = models.CharField(max_length=20, choices=TIPO_COBRO_CHOICES, verbose_name="Tipo de Cobro", null=True, blank=True)
    collection_discount = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Descuento Factoring (%)", null=True, blank=True)
    collection_bank = models.ForeignKey('extractos.ExtractosBancarios', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Extracto Bancario")
    collection_state = models.BooleanField(default=False, verbose_name="Factura Pagada")

