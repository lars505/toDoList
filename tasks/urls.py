from django.urls import path

from .views import index, agregar, eliminar, editar, login_view, register, logout_user

urlpatterns = [
    path("", index, name="index"),
    path("agregar/", agregar, name="agregar" ),
    path("eliminar/<int:id>", eliminar, name="eliminar" ),
    path("editar/<int:id>", editar, name="editar" ),
    path("login", login_view, name="login" ),
    path("register", register, name="register" ),
    path("logout", logout_user, name="logout" ),
]
