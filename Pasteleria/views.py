from django.shortcuts import render
from .models import Pasteles
from .forms import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms 
from django.views.generic import ListView, DetailView 
from django.contrib.messages.views import SuccessMessageMixin 
from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def listar(request):
    pasteles= Pasteles.objects.all()
    template="listar.html"
    context={
        'pasteles': pasteles,

    }
    return render (request,template,context)

def pastelcrear(request): 
    if request.method=='POST':
        form= agregar(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar')

    form = agregar 
    context={
        'form':form,

    }
    return render (request, "agregar.html", context)
def eliminar(request, id):
  member = Pasteles.objects.get(id=id)
  member.delete()
  return redirect(reverse('listar'))

def actualizar(request, id):
    if request.method=='POST':
        instance=Pasteles.objects.get(id=id)
        form=agregar(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('listar')
    
    dato = Pasteles.objects.get(id=id)
    #form= agregar()
    #form=mymember
    template = 'actualizar.html'
    context = {
    'dato': dato,
    #'form':form,
    }
    return render(request, template, context)
