from django.db import models
from  django.conf import settings
from django.core.validators import MinValueValidator

# Create your models here.
class carro(models.Model):
    color=models.CharField(max_length=20, blank=True, null=True)
    modelo= models.CharField(max_length=20, blank=True, null=True)
    anio= models.IntegerField()
    marca=models.CharField(max_length=20, blank=True, null=True)