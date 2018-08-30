from .models import Seguridad
from rest_framework import serializers

class ModuloSerializado(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Seguridad
        fields = ('id','Usuario','Huella','Email')

