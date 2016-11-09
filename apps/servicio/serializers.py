from rest_framework.serializers import ModelSerializer
from .models import Categoria, Usuario, Empresa
from .models import Servicio, Comentario, Pedido, Pago


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id',
                  'nombre',
                  'descripcion',
                  'imagen'
                  )


class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'direccion',
            'telefono',
            'celular',
            'password'
        )

    def create(self, validate_date):
        password = validate_date.get('password')
        instance = super().create(validate_date)
        instance.set_password(password)
        return instance


class EmpresaSerializer(ModelSerializer):
    class Meta:
        model = Empresa
        fields = (
            'id',
            'nombre',
            'descripcion',
            'logo',
            'direccion',
            'telefono',
            'nit',
            'usuario',
        )


class ServicioSerializer(ModelSerializer):
    class Meta:
        model = Servicio
        fields = (
            'id',
            'nombre',
            'descripcion',
            'imagen',
            'tipo_tiempo',
            'tiempo',
            'valor',
            'empresa',
            'categoria'
        )


class ComentarioSerializer(ModelSerializer):
    class Meta:
        model = Comentario
        fields = (
            'id',
            'valor',
            'descripcion',
            'usuario',
            'servicio'
        )


class PedidoSerializer(ModelSerializer):
    class Meta:
        model = Pedido
        fields = (
            'id',
            'comentario',
            'tiempo',
            'cantidad',
            'total',
            'usuario',
            'servicio'
        )
