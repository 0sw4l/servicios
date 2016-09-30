from django.contrib import admin
from .models import Cliente
from .forms import ClienteForm
# Register your models here.

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
	list_display = ['get_full_name', 'direccion', 'celular']
	form = ClienteForm