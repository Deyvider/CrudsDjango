from django.shortcuts import render
from .models import Pizza
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
    pizza= Pizza.objects.all()
    template="listarPi.html"
    context={
        'Pizza': pizza,

    }
    return render (request,template,context)

def pizzacrear(request): 
    if request.method=='POST':
        form= agregar(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarPi')  

    form = agregar 
    context={
        'form':form,

    }
    return render (request, "agregarPi.html", context)
def eliminar(request, id):
  member = Pizza.objects.get(id=id)
  member.delete()
  return redirect(reverse('listarPi'))

def actualizar(request, id):
    if request.method=='POST':
        instance=Pizza.objects.get(id=id)
        form=agregar(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('listarPi')
    
    dato = Pizza.objects.get(id=id)
    #form= agregar()
    #form=mymember
    template = 'actualizarPi.html'
    context = {
    'dato': dato,
    #'form':form,
    }
    return render(request, template, context)
