from rest_framework.serializers import ModelSerializer
from .models import Cliente


class ClienteSerializer(ModelSerializer):
	class Meta:
		model = Cliente
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


