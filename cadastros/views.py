from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .models import Usuario, Midia


class IndexView(TemplateView):
    template_name = "cadastros/index.html"


class UsuarioCreate(CreateView):
    model = Usuario
    fields = ["nome", "sobrenome", "email", "senha"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("cadastrar-usuario")
    extra_context = {"titulo": "Cadastro de Usuario"}

class MidiaCreate(CreateView):
    model = Midia
    fields = ["nome", "arquivo"]
    success_url = reverse_lazy("cadastrar-midia")
    template_name = "cadastros/formupload.html"
    extra_context = {"titulo": "Cadastro de Midia"}
