# Generated by Django 3.2.3 on 2022-12-02 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pizeria', '0006_alter_pizza_costo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='Costo',
            field=models.DecimalField(decimal_places=2, max_digits=5, max_length=8),
        ),
    ]
