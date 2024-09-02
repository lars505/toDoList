from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Task


# Create your views here.
# tareas = []
# tareas_dict = {}

def index(request):
    context = {
        'tareas': Task.objects.all() #select * from Tasks
    }
    return render(request, 'tasks/index.html', context)

def agregar(request):
    if request.method == "POST":
        tarea_text = request.POST.get("tarea")
        Task.objects.create(nombre=tarea_text) # Inser into Tasks () values()
        return redirect('index')
    return redirect('index')

def eliminar(request, id):
    tarea = Task.objects.filter(pk=id) #select * from tasks where id = id
    print(tarea)
    # if request.method == 'POST':
    tarea.delete()
    return redirect('index')

    # return redirect('index')

def editar(request, id):
    tarea = get_object_or_404(Task, id= id)
    if request.method == 'POST':
        tarea.nombre = request.POST.get('tarea')
        tarea.save()
        return redirect("index")
    return render(request,'tasks/editar.html', {'tarea': tarea.nombre} )
    