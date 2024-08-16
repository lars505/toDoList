from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.
# tareas = []
tareas_dict = {}

def index(request):
    context = {
        'tareas': tareas_dict
    }
    return render(request, 'tasks/index.html', context)

def agregar(request):
    if request.method == "POST":
        tarea_id = len(tareas_dict) + 1
        print(f'Esto es lo que contiene tarea id: {tarea_id}')
        tarea_text = request.POST.get("tarea")
        tareas_dict[tarea_id] = { "tarea": tarea_text, "completado": False}
        return redirect('index')
    return redirect('index')

def eliminar(request, id):
    if id in tareas_dict:
        del tareas_dict[id]
    return redirect('index')

def editar(request, id):
    if request.method == 'POST':
        tarea = request.POST.get('tarea')
        tareas_dict[id]['tarea']=tarea
        return redirect("index")
    return render(request,'tasks/editar.html', {'tarea_id': id, 'tarea': tareas_dict[id], 'tareas': tareas_dict} )
    