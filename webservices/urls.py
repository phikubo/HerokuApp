
from django.urls import path, include

from rest_framework import routers
from visualrec.models import *
#from . views import *
from webservices.views import *

router=routers.DefaultRouter()

router.register(r'venta_articulo', producto_viewset)
'''router.register(r'precios', precios_viewset)
router.register(r'descripcion', descripcion_viewset)'''

app_name='webservs'
urlpatterns = [
    #http://127.0.0.1:8000/webservices/api
    path('api/', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]
