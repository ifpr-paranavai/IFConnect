from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=55)
    sobrenome = models.CharField(max_length=55)
    email = models.EmailField(max_length=55)
    senha = models.CharField(max_length=15)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

class Midia(models.Model):
    nome = models.CharField(max_length=55)
    dataInicio = models.DateTimeField(editable=True)
    dataTermino = models.DateTimeField(editable=True)
    arquivo = models.ImageField(upload_to='imagens')
    #path = models.CharField(max_length=255)
    #status = models.BooleanField

class Tipo(models.Model):
    tipo = models.CharField(max_length=55)