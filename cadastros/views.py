import os
from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DeleteView
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
    fields = ["nome", "arquivo", "dataInicio", "dataTermino"]
    success_url = reverse_lazy("cadastrar-midia")
    template_name = "cadastros/formupload.html"
    extra_context = {"titulo": "Cadastro de Midia"}


class MidiaList(ListView):
    model = Midia
    template_name = "cadastros/list/midia.html"
    paginate_by = 10


class MidiaDeleteView(DeleteView):
    model = Midia
    template_name = 'cadastros/delete_midia.html'
    success_url = reverse_lazy('listar-midia')


def delete_midia(request, midia_id):
    midia = get_object_or_404(Midia, pk=midia_id)
    if request.method == 'POST':
        midia.delete()
        return redirect('nome_da_view_list')
    return render(request, 'cadastros/delete_midia.html', {'midia': midia})
