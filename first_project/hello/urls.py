# Importar una biblioteca 
# administradora de rutas
from django.urls import path

# Importando vistas
from . import views

# declarando las rutas validas
urlpatterns = [
    # Get /hello/
    path("", views.index, name="index"),
    # Get /hello/autor
    path("author/", views.author, name="author"),
]

