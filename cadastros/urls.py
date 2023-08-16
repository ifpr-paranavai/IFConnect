from django.urls import path
from .views import UsuarioCreate, MidiaCreate



urlpatterns = [
    path("cadastrar/usuario", UsuarioCreate.as_view(), name="cadastrar-usuario"),
    path("cadastrar/midia", MidiaCreate.as_view(), name= "cadastrar-midia"),
]
