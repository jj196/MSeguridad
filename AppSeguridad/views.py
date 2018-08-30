# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import  generics
from .models import Seguridad
from .Serializador import  ModuloSerializado
from django.shortcuts import   get_object_or_404


# Create your views here.
class ListaHuellas(generics.ListCreateAPIView):
    queryset = Seguridad.objects.all()
    serializer_class = ModuloSerializado

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj
