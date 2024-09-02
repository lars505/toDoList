from django.db import models

# Create your models here.

class Task (models.Model):
    nombre = models.CharField(max_length=100) #campo para el nombre de la tarea.
    estado = models.BooleanField(default=False) # campo para cambiar de estado del dato.

    created_at = models.DateTimeField(auto_now_add=True) #campo para la fecha de creacion.
    updated_at = models.DateTimeField(auto_now=True) #campo para guardar la ultima fehca de actualizcion.

    def __str__(self):
        return  f'{self.nombre}'