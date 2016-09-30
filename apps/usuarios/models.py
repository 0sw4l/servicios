from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cliente(User):
	direccion = models.CharField(max_length=50)
	telefono = models.CharField(max_length=20)
	celular = models.CharField(max_length=20)

	class Meta:
		verbose_name = 'Cliente'
		verbose_name_plural = 'Clientes'
