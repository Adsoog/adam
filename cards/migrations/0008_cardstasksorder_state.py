# Generated by Django 5.0.3 on 2024-07-24 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0007_alter_cards_valuation'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardstasksorder',
            name='state',
            field=models.BooleanField(default=False),
        ),
    ]
