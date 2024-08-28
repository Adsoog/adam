from django.db import models
from .utils import rename_file
from projects.models import Project 

class Station(models.Model):
    project = models.ForeignKey(Project, related_name='stations', on_delete=models.CASCADE, verbose_name="Proyecto")
    name = models.CharField(max_length=100, verbose_name="Nombre de la Estación")
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.project.project_name}"

class Photo(models.Model):
    station = models.ForeignKey(Station, related_name='photos', on_delete=models.CASCADE, verbose_name="Estación")
    image = models.ImageField(upload_to='station_photos/')
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.image:
            # Modificar el nombre del archivo antes de guardarlo
            self.image.name = rename_file(self, self.image.name, 'station_photos/')
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Foto en {self.station.name} del Proyecto {self.station.project.project_name}"


class Document(models.Model):
    station = models.ForeignKey(Station, related_name='documents', on_delete=models.CASCADE, verbose_name="Estación")
    file = models.FileField(upload_to='station_documents/')
    description = models.CharField(blank=True, null=True, max_length=100, verbose_name="Nombre del Documento")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.file:
            # Modificar el nombre del archivo antes de guardarlo
            self.file.name = rename_file(self, self.file.name, 'station_documents/')
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.description} - {self.station.name}"


class Attendance(models.Model):
    station = models.ForeignKey(Station, related_name="attendance_records", on_delete=models.CASCADE, verbose_name="Estación")
    attendance_record = models.FileField(upload_to='station_attendance/')
    description = models.CharField(blank=True, null=True, max_length=100, verbose_name="Tareo del Día")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.attendance_record:
            # Modificar el nombre del archivo antes de guardarlo
            self.attendance_record.name = rename_file(self, self.attendance_record.name, 'station_attendance/')
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.description} - {self.station.name}"
