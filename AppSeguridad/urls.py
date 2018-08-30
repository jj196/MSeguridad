from django.conf.urls import url
from AppSeguridad.views import *

urlpatterns = [
    url(r'^AppSeguridad/$', ListaHuellas.as_view(), name='AppSeguridad')
]