# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from riak import RiakClient, RiakNode 
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

# Create your views here.

RiakClient()
RiakClient(protocol='http', host='127.0.0.1', http_port=8098)
RiakClient(nodes=[{'host':'127.0.0.1','http_port':8098}])

myClient  = RiakClient()
myBucket = myClient.bucket('users')

def home(request):
    function = Functions.objects.all()
    return render(request, 'home.html', {'functions':function})

def salvar_function(request):
    titulo = request.POST.get('titulo')
    
    if titulo:
        functions = Functions()
        functions.titulo=titulo
        functions.save()
        return redirect('/functions')

def functions(request):
    functions = Functions.objects.all()
    return render(request, 'home.html', {'functions':functions})

def functionInsert(request, id):
    function = Functions.objects.get(id=id)
    return render(request, 'paraInsert.html', {'function':function})

def insert_function(request):
        RiakClient()
        RiakClient(protocol='http', host='127.0.0.1', http_port=8098)
        RiakClient(nodes=[{'host':'127.0.0.1','http_port':8098}])
        myClient  = RiakClient()
        myBucket = myClient.bucket('users')

        getNome = request.POST.get("name")
        getNome = str(getNome)
        getLocation = request.POST.get("location")
        getRole = request.POST.get("role")    
        getFulname = request.POST.get("fulname")            
        user4 = {
                'name' : str(getNome),
                'location': getLocation,
                'role': getRole,
                'fullname' : getFulname
        }
        obj = myBucket.new('user4',data=user4)
        obj.store()        
        return redirect('/home')

def categorias(request):    
    return render(request, 'addCategoria.html',)

def selection_function(request):    
        #clientes = myBucket.get_keys()
        #clientes = Clientes.objects.all()
        #nome = ''
        #locacao = ''
        #profissao = ''
        #apelido = ''
        for key in myBucket.get_keys():
                nome = myBucket.get(key).data['name']
                #clientes.nome = nome
                locacao = myBucket.get(key).data['location']
                #clientes.locacao = locacao
                profissao = myBucket.get(key).data['role']
                #clientes.profissao = profissao
                apelido = myBucket.get(key).data['fulname']
                #clientes.apelido = apelido
                return render(request, 'usuario.html', context = {'name':nome, 'location' : locacao, 'role' : profissao, 'fulname' : apelido})