from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TareaForm


# Create your views here.
# tareas = []
tareas_dict = {}

def index(request):
    context = {
        'tareas': tareas_dict,
        'form':TareaForm()
        
    }
    return render(request, 'tasks/index.html', context)

def agregar(request):
    if request.method == "POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea_id = len(tareas_dict) + 1
            tarea_text = form.cleaned_data["tarea"]
            tareas_dict[tarea_id] = { "tarea": tarea_text, "completado": False}
            return redirect('index')
    return redirect('index')

def eliminar(request, id):
    if id in tareas_dict:
        del tareas_dict[id]
    return redirect('index')

def editar(request, id):
    if id not in tareas_dict:
        return redirect('index')
    
    tarea = tareas_dict[id]

    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tareas_dict[id]['tarea'] = form.cleaned_data['tarea']
            return redirect("index")
    else:
        form = TareaForm(initial={
            'tarea': tarea["tarea"]
        })
    context = {
        'form':form,
        'tareas': tareas_dict,
        'id': id,
    }
    return render(request,'tasks/editar.html', context )
    