from django.db import models
from  django.conf import settings


# Create your models here.
class Pasteles(models.Model):
    Sabor=models.CharField(max_length=20, blank=True, null=True)
    Medida= models.CharField(max_length=20, blank=True, null=True)
    Cantidad= models.IntegerField()
    Costo=models.IntegerField()