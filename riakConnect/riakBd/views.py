# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from random import randint
from riak import RiakClient, RiakNode 
import uuid
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
        getFulname = request.POST.get("fullname")            
        nome = str('user')+str(randint(0,9))
        nome = {
                'name' : getNome,
                'location': getLocation,
                'role': getRole,
                'fullname' : getFulname
        }
        
        obj = myBucket.new(str(nome),data=nome)
        obj.store()           
        return redirect('/home')

def categorias(request):     
    return render(request, 'addCategoria.html',)

def selection_function(request):    
        RiakClient()
        RiakClient(protocol='http', host='127.0.0.1', http_port=8098)
        RiakClient(nodes=[{'host':'127.0.0.1','http_port':8098}])
        myClient  = RiakClient()
        myBucket = myClient.bucket('users')
        
        keys = myBucket.get_keys()       
        usuarios = Clientes()        


        lista2 = []
        for i in range(len(keys)):
            lista = {
                'name': myBucket.get(keys[i]).data['name'],
                'location': myBucket.get(keys[i]).data['location'],
                'role': myBucket.get(keys[i]).data['role'],
                'fullname' : myBucket.get(keys[i]).data['fullname']
            }
            lista2.append(lista)

        # for i in range(len(lista1)):                                    
        #     #lista.append(myBucket.get(keys[i]).data['name'])
        #     usuarios.nome = str(lista1[i][0])
        #     #lista.append(myBucket.get(keys[i]).data['location'])
        #     usuarios.locacao = str(lista1[i][1])
        #     #lista.append(myBucket.get(keys[i]).data['role'])
        #     usuarios.profissao = str(lista1[i][2])
        #     #lista.append(myBucket.get(keys[i]).data['fulname'])
        #     usuarios.apelido = str(lista1[i][3])
        #     usuarios.save()
            

        usuarios = Clientes.objects.all()
        return render(request, 'usuario.html',  {'usuarios': lista2})
