from django.db import models
from rest_framework import serializers
from visualrec.models import *
# Create your models here.

class producto_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=venta_articulo
        fields=('titulo', 'precio', 'marca_carros', 'descripcion', 'foto',)