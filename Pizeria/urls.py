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
    path('Pizza/',listar,name="listarPi"),
    path('crearPi/', pizzacrear, name='crearPi'),
    path('eliminarPi/<int:id>',eliminar,name='eliminarPi'),
    path('actualizarPi/<int:id>',actualizar,name='actualizarPi'),
]