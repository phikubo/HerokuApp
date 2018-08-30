
from django.urls import path
from . import views
app_name='appvr'
urlpatterns = [
    #http://127.0.0.1:8000/miwatson/publicar
    path('publicar/', views.index, name='inicio'),
    # http://127.0.0.1:8000/miwatson/visualizar/<id del producto>
    path('visualizar/<int:id_producto>', views.ver_item_view, name='visualizar'),
    #
    # http://127.0.0.1:8000/miwatson/login/
    path('login/',views.ingresar,name='login'),
    path('logout/',views.salido,name='logout'),
    # http://127.0.0.1:8000/miwatson/listar/
    path('listar/',views.listar, name='listar'),
    path('registrar/',views.registrar_view,name='registrar'),
    path('servicio_web/', views.servicio_web,name='servicio'),

]
