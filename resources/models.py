from django.db import models

class Resource(models.Model):
    RESOURCE_TYPES = [
        ('calidad', 'Calidad'),
        ('seguridad', 'Seguridad'),
    ]
    resource = models.CharField(max_length=100)
    resource_type = models.CharField(max_length=10, choices=RESOURCE_TYPES, default='calidad', verbose_name="Tipo de Recurso")


    def __str__(self):
        return self.resource

class Hazard(models.Model):
    hazard = models.CharField(max_length=100)
    resources = models.ManyToManyField(Resource, related_name='hazards')

    def __str__(self):
        return self.hazard
    
class Risk(models.Model):
    hazard = models.OneToOneField(Hazard, on_delete=models.CASCADE, related_name='risk')
    description = models.CharField(max_length=100)

    def __str__(self):
        return f"Risk associated with {self.hazard.name}"

class Cause(models.Model):
    hazard = models.OneToOneField(Hazard, on_delete=models.CASCADE, related_name='cause')
    description = models.CharField(max_length=100)

    def __str__(self):
        return f"Cause for {self.hazard.name}"

class Control(models.Model):
    hazard = models.OneToOneField(Hazard, on_delete=models.CASCADE, related_name='control')
    measures = models.CharField(max_length=100)

    def __str__(self):
        return f"Control measures for {self.hazard.name}"
    