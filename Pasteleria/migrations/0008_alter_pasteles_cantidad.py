# Generated by Django 3.2.3 on 2022-12-02 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pasteleria', '0007_auto_20221202_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pasteles',
            name='Cantidad',
            field=models.IntegerField(blank=True, max_length=3, null=True),
        ),
    ]
