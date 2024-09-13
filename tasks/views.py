from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Task, CuatomUser

from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import login, logout, authenticate


# Create your views here.
# tareas = []
# tareas_dict = {}
@login_required
def index(request):
    context = {
        'tareas': Task.objects.filter(user = request.user ) #select * from Tasks
    }
    return render(request, 'tasks/index.html', context)

@login_required
def agregar(request):
    if request.method == "POST":
        tarea_text = request.POST.get("tarea")
        Task.objects.create(user= request.user, nombre=tarea_text) # Inser into Tasks () values()
        return redirect('index')
    return redirect('index')

@login_required
def eliminar(request, id):
    tarea = Task.objects.filter(pk=id) #select * from tasks where id = id
    print(tarea)
    # if request.method == 'POST':
    tarea.delete()
    return redirect('index')

    # return redirect('index')

@login_required
def editar(request, id):
    tarea = get_object_or_404(Task, id= id)
    if request.method == 'POST':
        tarea.nombre = request.POST.get('tarea')
        tarea.save()
        return redirect("index")
    return render(request,'tasks/editar.html', {'tarea': tarea.nombre} )
    
    
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        print(username, password)
        
        user = authenticate(request, username= username, password = password)
        print(user)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "tasks/login.html" )
        
    return render(request, "tasks/login.html")
            
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        
        if username and password and password2:
            if password == password:
                try:
                    user = CuatomUser.objects.create_user(username = username, password = password)
                    print(user)
                    login(request, user)
                    return redirect('index')
                except Exception as e:
                    print("Este es el error" +  e)
            else:
                print("Las contraseñas no son iguales")
        else:
            print("Ingrese los campos necesarios")
            
    return render(request, "tasks/register.html")
  
def logout_user(request):
    logout(request)   
    return redirect("index")           
            
            
        
    