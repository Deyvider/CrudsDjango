# Generated by Django 3.2.3 on 2022-12-01 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pasteleria', '0002_alter_pasteles_costo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pasteles',
            name='Medida',
            field=models.CharField(blank=True, default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pasteles',
            name='Sabor',
            field=models.CharField(blank=True, default=0, max_length=20),
            preserve_default=False,
        ),
    ]
