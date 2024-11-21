

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea
from .forms import TareaForm

def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'tareas/lista_tareas.html', {'tareas': tareas})

def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')
    else:
        form = TareaForm()
    return render(request, 'tareas/crear_tarea.html', {'form': form})

def editar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')
    else:
        form = TareaForm(instance=tarea)
    return render(request, 'tareas/editar_tarea.html', {'form': form})

def eliminar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    if request.method == 'POST':
        tarea.delete()
        return redirect('lista_tareas')
    return render(request, 'tareas/eliminar_tarea.html', {'tarea': tarea})

