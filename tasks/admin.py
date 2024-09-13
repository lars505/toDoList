from django.contrib import admin
from .models import Task as tarea, CuatomUser

class task_admin(admin.ModelAdmin):
    list_display = ["nombre", "created_at", "estado"]
    list_filter = ["nombre","estado"]
    search_fields = ["nombre"]
    list_editable = ["estado"]
# Register your models here.
admin.site.register(tarea, task_admin)
admin.site.register(CuatomUser)
