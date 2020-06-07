from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Todo
from .forms import TodoForm

def index(request):              #display todo page
    todo_list = Todo.objects.order_by('id')

    form = TodoForm()

    context = {'todo_list' : todo_list, 'form' : form}

    return render(request, 'todo/index.html', context)

@require_POST                   #add task to todo
def addTodo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        new_todo = Todo(text=request.POST['text'] ,
                        priority=request.POST['priority'],
                        type=request.POST['type'],
                        duedate=request.POST['duedate'])
        new_todo.save()

    return redirect('index')

def completeTodo(request, todo_id): #mark completed task from todo
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('index')

def deleteCompleted(request):   #delete compelted task
    Todo.objects.filter(complete__exact=True).delete()

    return redirect('index')

def deleteAll(request):         #delete all tasks
    Todo.objects.all().delete()

    return redirect('index')
