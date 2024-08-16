from django.urls import path

from .views import index, agregar, eliminar, editar

urlpatterns = [
    path("", index, name="index"),
    path("agregar/", agregar, name="agregar" ),
    path("eliminar/<int:id>", eliminar, name="eliminar" ),
    path("editar/<int:id>", editar, name="editar" ),
]
