# Generated by Django 3.2.3 on 2022-11-28 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pasteles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sabor', models.CharField(blank=True, max_length=20, null=True)),
                ('Medida', models.CharField(blank=True, max_length=20, null=True)),
                ('Cantidad', models.IntegerField()),
                ('Costo', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
