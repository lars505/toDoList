from django.urls import path

from .views import index, agregar, eliminar, editar

urlpatterns = [
    path("", index, name="index"),
    path("agregar/", agregar, name="agregar" ),
    path("eliminar/<str:nombre>", eliminar, name="eliminar" ),
    path("editar/<str:nombre>", editar, name="editar" ),
]
