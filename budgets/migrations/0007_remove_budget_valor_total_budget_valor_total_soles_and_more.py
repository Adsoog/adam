# Generated by Django 5.0.2 on 2024-08-11 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0006_budgetitem_precio_item_proyecto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budget',
            name='valor_total',
        ),
        migrations.AddField(
            model_name='budget',
            name='valor_total_soles',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='budget',
            name='tipo_cambio',
            field=models.DecimalField(decimal_places=3, default=3.75, max_digits=10),
        ),
        migrations.AlterField(
            model_name='budget',
            name='valor_total_usd',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
    ]
