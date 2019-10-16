# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Clientes(models.Model):    
    nome = models.CharField('name', max_length=150)
    locacao = models.CharField('location', max_length=150)
    profissao = models.CharField('role', max_length=150)
    apelido = models.CharField('fulname', max_length=150)

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    titulo = models.CharField('titulo', max_length=50)
    descricao = models.TextField()

    def __str__(self):
        return self.titulo

class Functions(models.Model):
    titulo = models.CharField('titulo', max_length=250)                

    def __str__(self):
        return self.titulo  



