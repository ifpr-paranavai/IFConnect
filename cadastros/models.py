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
    dataInicio = models.DateField()
    dataTermino = models.DateField()
    arquivo = models.ImageField(upload_to='uploads')
    #path = models.CharField(max_length=255)
    #status = models.BooleanField

    def delete(self, *args, **kwargs):
        
        self.arquivo.delete()
        super().delete(*args, **kwargs)

class Tipo(models.Model):
    tipo = models.CharField(max_length=55)