from django.db import models
from  django.conf import settings


# Create your models here.
class Pizza(models.Model):
    Nombre=models.CharField(max_length=20, blank=True, null=True)
    Medida= models.CharField(max_length=20, blank=True, null=True)
    Cantidad= models.IntegerField()
    Costo=models.IntegerField()