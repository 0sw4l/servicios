from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CategoriaSerializer, UsuarioSerializer, EmpresaSerializer, ServicioSerializer
from .models import Categoria, Empresa, Servicio


class CategoriaView(APIView):
    def get(self, request, format=None):
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response({'categorias': serializer.data})

    def post(self, request, format=None):
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "success": "se creo la categoria : {0}".format(
                    serializer.data['nombre']
                )}
                , status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsuarioView(APIView):
    def get(self, request, format=None):
        return Response('Bienvenido a mi API :)')

    def post(self, request, format=None):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'success': False
            }, status=status.HTTP_201_CREATED)


class EmpresaView(APIView):
    def get(self, request, format=None):
        empresas = Empresa.objects.all()
        serializer = EmpresaSerializer(empresas, many=True)
        return Response({
            'empresas': serializer.data
        }, status=status.HTTP_200_OK)


class ServicioView(APIView):
    def get(self, request, format=None):
        servicios = Servicio.objects.all()
        serializer = ServicioSerializer(servicios, many=True)
        return Response({
            'servicios': serializer.data
        }, status=status.HTTP_202_ACCEPTED)

