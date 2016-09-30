from django.conf.urls import url
from .views import ClienteView

urlpatterns = [
   url(r'^clientes/', ClienteView.as_view())
]
