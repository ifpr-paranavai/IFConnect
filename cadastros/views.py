import os
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DeleteView
from .models import Usuario, Midia
from django.contrib.auth.mixins import LoginRequiredMixin



class IndexView(TemplateView, LoginRequiredMixin):
    template_name = "cadastros/index.html"


class UsuarioCreate(CreateView, LoginRequiredMixin):
    model = Usuario
    fields = ["nome", "sobrenome", "email", "senha"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("cadastrar-usuario")
    extra_context = {"titulo": "Cadastro de Usuario"}


class MidiaCreate(CreateView, LoginRequiredMixin):
    model = Midia
    fields = ["nome", "arquivo", "dataInicio", "dataTermino"]
    success_url = reverse_lazy("cadastrar-midia")
    template_name = "cadastros/formupload.html"
    extra_context = {"titulo": "Cadastro de Midia"}


class MidiaList(ListView, LoginRequiredMixin):
    model = Midia
    template_name = "cadastros/list/midia.html"
    paginate_by = 10


class MidiaDeleteView(DeleteView, LoginRequiredMixin):
    model = Midia
    template_name = 'cadastros/delete_midia.html'
    success_url = reverse_lazy('listar-midia')

def delete_midia(request, midia_id):
    arquivo = get_object_or_404(Midia, pk=midia_id)
    if request.method == 'POST':
        arquivo.delete()
        return redirect('listar-midia')
    return render(request, 'cadastros/delete_midia.html', {'midia': arquivo})


