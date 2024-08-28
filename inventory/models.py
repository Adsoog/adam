from django.db import models

class BaseInventario(models.Model):
    num_articulo = models.CharField(max_length=50, verbose_name="Número de Articulo")
    descripcion = models.CharField(max_length=255, verbose_name="Descripción")
    en_stock = models.IntegerField(default=0, verbose_name="Stock")
    codigo_barras = models.CharField(max_length=100, blank=True, default='', verbose_name="Código de Barras")
    grupo_articulos = models.CharField(max_length=100, default='MISC', verbose_name="Grupo de Articulos")
    fabricante = models.CharField(max_length=100, blank=True, default='', verbose_name="Fabricante")
    unidad_medida = models.CharField(max_length=50, blank=True, default='', verbose_name="Unidad de Medida")
    precio_unitario_diario = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Precio Unitario Diario")
    ultimo_precio_compra = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Ultimo Precio de Compra")

    class Meta:
        abstract = True

    def __str__(self):
        return self.descripcion

class Equipos(BaseInventario):
    grupo_articulos = models.CharField(max_length=100, default='EQUIPOS')

class EPPS(BaseInventario):
    grupo_articulos = models.CharField(max_length=100, default='EPPS')

class Transporte(BaseInventario):
    grupo_articulos = models.CharField(max_length=100, default='TRANSPORTE')

class Materiales(BaseInventario):
    grupo_articulos = models.CharField(max_length=100, default='MATERIALES')

class Consumibles(BaseInventario):
    grupo_articulos = models.CharField(max_length=100, default='CONSUMIBLES')

class Alimentos(BaseInventario):
    grupo_articulos = models.CharField(max_length=100, default='ALIMENTOS')

class ManoDeObra(BaseInventario):
    grupo_articulos = models.CharField(max_length=100, default='MANODEOBRA')

class Herramientas(BaseInventario):
    grupo_articulos = models.CharField(max_length=100, default='HERRAMIENTAS')

class Misc(BaseInventario):
    grupo_articulos = models.CharField(max_length=100, default='MISC')
