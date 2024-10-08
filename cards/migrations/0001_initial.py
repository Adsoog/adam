# Generated by Django 5.0.3 on 2024-07-19 01:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('resources', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verb', models.CharField(max_length=100)),
                ('object', models.CharField(max_length=100)),
                ('orden_venta', models.CharField(db_index=True, max_length=200)),
                ('client', models.CharField(default='', max_length=200)),
                ('measurement', models.CharField(default='minutos', max_length=50)),
                ('task_time', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('cards', models.ManyToManyField(related_name='tasks', to='cards.cards')),
                ('resources', models.ManyToManyField(related_name='task_resource', to='resources.resource')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
