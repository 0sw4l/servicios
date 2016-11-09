from django.contrib.auth.models import User
from django.db import models


class BaseState(models.Model):
    estado = models.IntegerField(default=1, editable=False)

    class Meta:
        abstract = True


class Categoria(BaseState):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()
    imagen = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Usuario(User):
    celular = models.CharField(max_length=15)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=30)
    role = models.CharField(max_length=20)

    def __str__(self):
        return self.get_full_name()


class Empresa(BaseState):
    nombre = models.CharField(max_length=30, unique=True)
    descripcion = models.TextField()
    logo = models.URLField()
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    nit = models.CharField(max_length=20, unique=True)
    usuario = models.ForeignKey(Usuario)


class Servicio(BaseState):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()
    imagen = models.URLField()
    tipo_tiempo = models.CharField(max_length=4)
    tiempo = models.IntegerField()
    valor = models.FloatField()
    empresa = models.ForeignKey(Empresa)
    categoria = models.ForeignKey(Categoria)


class Comentario(BaseState):
    valor = models.IntegerField()
    descripcion = models.TextField()
    usuario = models.ForeignKey(Usuario)
    servicio = models.ForeignKey(Servicio)


class Pedido(BaseState):
    comentario = models.TextField()
    tiempo = models.DateTimeField()
    cantidad = models.IntegerField()
    total = models.FloatField()
    usuario = models.ForeignKey(Usuario)
    servicio = models.ForeignKey(Servicio)


class Pago(BaseState):
    tiempo = models.DateTimeField()
    total = models.IntegerField()
    usuario = models.ForeignKey(Usuario)
    pedido = models.ForeignKey(Pedido)
    empresa = models.ForeignKey(Empresa)


