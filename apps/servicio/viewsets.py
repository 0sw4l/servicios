from rest_framework.response import Response
from rest_framework.decorators import detail_route
from rest_framework import viewsets

from apps.servicio.models import Categoria, Servicio
from apps.servicio.serializers import CategoriaSerializer, ServicioSerializer


class CategoriaViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    @detail_route(methods=['get'])
    def servicios(self, request, pk=None):
        servicios = Servicio.objects.filter(categoria_id=pk)
        serializer = ServicioSerializer(servicios, many=True)
        return Response(serializer.data)