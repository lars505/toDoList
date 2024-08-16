from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.
tareas = []

def index(request):
    context = {
        'tareas': tareas
    }
    return render(request, 'tasks/index.html', context)

def agregar(request):
    tarea = request.POST.get('tarea')
    if tarea:
        tareas.append(tarea)
    else:
        print("Esciba un valor valido!")
        return redirect('index')
    return redirect('index')

def eliminar(request, nombre):
    tareas.remove(nombre)
    return redirect('index')

def editar(request, nombre):
    
    return render(request, "tasks/index.html", {"tarea":nombre, "tareas":tareas})