from django.urls import path, include
from .views import IndexView, UsuarioCreate



urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("cadastrar/usuario", UsuarioCreate.as_view(), name="cadastrar-usuario"),

]
