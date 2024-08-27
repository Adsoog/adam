# Generated by Django 5.0.2 on 2024-08-17 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_remove_project_end_date_remove_project_start_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='sap_code',
        ),
        migrations.AlterField(
            model_name='project',
            name='ov_name',
            field=models.CharField(max_length=100, verbose_name='Oferta de Venta'),
        ),
    ]
