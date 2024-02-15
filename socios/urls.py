# socios/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('introducir-socio/', views.introducir_socio, name='introducir_socio'),
    path('modificar-socio/<int:numero_socio>/', views.modificar_socio, name='modificar_socio'),
    path('obtener-todos-los-socios/', views.obtener_todos_los_socios, name='obtener_todos_los_socios'),
]
