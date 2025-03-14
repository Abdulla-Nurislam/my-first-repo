from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Todo
from .forms import TodoForm

@login_required
def todo_list(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todos/todo_list.html', {'todos': todos})

@login_required
def todo_detail(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    return render(request, 'todos/todo_detail.html', {'todo': todo})

@login_required
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todos/todo_form.html', {'form': form})

@login_required
def todo_delete(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    todo.delete()
    return redirect('todo_list') 