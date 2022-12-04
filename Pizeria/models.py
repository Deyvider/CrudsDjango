from django.db import models
from  django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Pizza(models.Model):
    Nombre=models.CharField(max_length=20, blank=False, null=False)
    Medida= models.CharField(max_length=20, blank=False, null=False)
    Cantidad= models.IntegerField(blank=False, null=False, validators=[MinValueValidator(0),MaxValueValidator(1000)])
    Costo=models.DecimalField(max_digits=5, max_length=8, blank=False, null=False,decimal_places=2)