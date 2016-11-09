from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from apps.utils.models import BaseUser


class Cliente(BaseUser):
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
