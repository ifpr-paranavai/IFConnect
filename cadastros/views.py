from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .models import Usuario


class IndexView(TemplateView):
    template_name = "cadastros/index.html"


class UsuarioCreate(CreateView):
    model = Usuario
    fields = ["nome", "sobrenome", "email", "senha"]
    template_name = "cadastros/form.html"
    #success_url = reverse_lazy("cadastrar-usuario")
    extra_context = {"titulo": "Cadastro de Usuario"}
