from django.contrib import admin
from django.urls import path
from .views import *
import re
from django.views.static import serve
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url, include
from .views import *



urlpatterns = [
    path('listarP/',listar,name="listarP"),
    path('crearP/', pizzacrear, name='crearP'),
    path('eliminarP/<int:id>',eliminar,name='eliminarP'),
    path('actualizarP/<int:id>',actualizar,name='actualizarP'),
]