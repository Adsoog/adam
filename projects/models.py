from django.db import models
from datetime import date

class Contractor(models.Model):
    contractor_name = models.CharField(max_length=100, verbose_name="Nombre de Contratista")
    address = models.CharField(max_length=150, verbose_name="Dirección")
    phone = models.CharField(max_length=20, verbose_name="Teléfono")
    contractor_ruc = models.CharField(max_length=20, verbose_name="RUC del Contratista") 
    email = models.EmailField()

    def __str__(self):
        return self.contractor_name
    
class Client(models.Model):
    client_name = models.CharField(max_length=100, verbose_name="Nombre del cliente")
    email = models.EmailField(default='')
    phone = models.CharField(max_length=20,default='', verbose_name="Teléfono")
    client_ruc = models.CharField(max_length=50, verbose_name="Ruc del cliente", default='')
    contact = models.CharField(max_length=50, verbose_name="Contacto", default='')

    def __str__(self):
        return self.client_name

class Project(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Clientes")
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE,verbose_name="Contratista")
    project_name = models.CharField(max_length=100, verbose_name="Nombre del projecto")
    ov_name = models.CharField(max_length=100, verbose_name="Oferta de Venta")
    
    @property
    def total_budget(self):
        total = sum(budget.total_dolares_final for budget in self.budgets.all())
        return total

    def __str__(self):
        return self.project_name

