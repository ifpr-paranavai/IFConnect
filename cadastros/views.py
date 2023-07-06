from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Usuario
# Create your views here.
class IndexView(TemplateView):
    template_name = "cadastros/index.html"


class UsuarioCreate(CreateView):
    model = Usuario
    fields = ["nome", "sobrenome", "email", "senha"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("cadastrar-usuario")
    extra_context = {"titulo": "Cadastro de Usuario"}
