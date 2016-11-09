from django.conf.urls import url, include

from apps.servicio.viewsets import CategoriaViewSet
from .views import CategoriaView, ServicioView, EmpresaView, UsuarioView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'categorias', CategoriaViewSet)

urlpatterns = [
    url(r'^usuarios/', UsuarioView.as_view()),
    url(r'^empresas/', EmpresaView.as_view()),
    url(r'^servicios/', ServicioView.as_view()),
    url(r'^', include(router.urls)),
]
