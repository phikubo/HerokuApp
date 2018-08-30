from django.shortcuts import render
#from .serializer import *
from visualrec.models import *
from rest_framework import viewsets

from webservices.serializer import *
# Create your views here.

class producto_viewset(viewsets.ModelViewSet):
    queryset = venta_articulo.objects.all()
    serializer_class=producto_serializer

'''   
class precios_viewset(viewset.ModelViewSet):
    queryset=marc.objects.all()
    serializer_class=marca_serializer

class descripcion_viewset(viewset.ModelViewSet):
    queryset=catego.objects.all()
    serializer_class=categoria_serializer'''