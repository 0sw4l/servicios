from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class BaseUser(User):
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    celular = models.CharField(max_length=20)

    class Meta:
        abstract = True
