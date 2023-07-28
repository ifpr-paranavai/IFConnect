from django.urls import path
from django.views import View
from .views import IndexView
from .views import UsuarioCreate



urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("cadastrar/usuario", UsuarioCreate.as_view(), name="cadastrar-usuario"),

]
