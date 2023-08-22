
from django.urls import path

from ifconnect import settings
from django.conf.urls.static import static
from .views import UsuarioCreate, MidiaCreate, MidiaList, MidiaDeleteView, delete_midia



urlpatterns = [
    path("cadastrar/usuario", UsuarioCreate.as_view(), name="cadastrar-usuario"),
    path("cadastrar/midia", MidiaCreate.as_view(), name= "cadastrar-midia"),
    path("listar/midia", MidiaList.as_view(), name="listar-midia"),
    path('midia/<int:midia_id>/delete/', delete_midia, name='midia-delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
