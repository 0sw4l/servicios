from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Cliente


class ClienteForm(UserCreationForm):
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
		)