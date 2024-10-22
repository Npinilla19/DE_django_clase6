from django.urls import path 
from . import views

urlpatterns = [
    path("lista/", views.listaEmpleados, name="lista"),
]