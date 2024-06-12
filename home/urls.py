from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name='home'),
    path('signup/', registro_view, name='registro'),
    path('login/',login_view, name='login'),
    path('logout/',cerrar_sesion, name='logout'),
    path('producto/upload',subir_producto, name='upload_product'),
]