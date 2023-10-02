from django.urls import path, include
from .views import IndexView, Inicio

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("inicio", Inicio.as_view(), name='inicio'),
    
]
