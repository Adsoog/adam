# Generated by Django 5.0.6 on 2024-06-09 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_contractor_contractor_ruc'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='ov_name',
            field=models.CharField(default=2024, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='sap_code',
            field=models.CharField(default=2024, max_length=50),
            preserve_default=False,
        ),
    ]
