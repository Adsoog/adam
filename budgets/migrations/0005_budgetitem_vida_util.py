# Generated by Django 5.0.2 on 2024-08-11 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0004_budgetitem_real_price_day_budgetitem_unidad_medida'),
    ]

    operations = [
        migrations.AddField(
            model_name='budgetitem',
            name='vida_util',
            field=models.PositiveIntegerField(default=365),
        ),
    ]
