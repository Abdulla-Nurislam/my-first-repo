from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from .forms import TodoForm
from django.forms.widgets import DateTimeInput

# Create your views here.

def todos_list(request):
    todos = Todo.objects.all().order_by('due_date')
    return render(request, 'todos/todos_list.html', {'todos': todos})

def todo_detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    return render(request, 'todos/todo_detail.html', {'todo': todo})

def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todos_list')
    else:
        form = TodoForm()
    return render(request, 'todos/todo_form.html', {'form': form})

def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todos_list')
    return render(request, 'todos/todo_delete.html', {'todo': todo})

def toggle_status(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.status = not todo.status
    todo.save()
    return redirect('todos_list')
