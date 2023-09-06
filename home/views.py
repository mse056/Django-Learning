from django.shortcuts import render, redirect
from .models import Todo
from django.contrib import messages
from .froms import TodoCreateForm, TodoUpdateForm

def sey_hello(request):
    person = {'name':'saleh'}
    return render(request, 'hello.html', context=person)

def home(request):
    return render(request, 'home.html')

def all_Todos(request):
    all = Todo.objects.all()
    return render(request, 'Todo.html', {'Todos':all})

def detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'detail.html', {'todo':todo})

def delete(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    messages.success(request, 'Todo deleted successfully', 'success')
    return redirect('Todos')

def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        form = TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'you todo updated successfully', 'success')
            return redirect('details', todo_id)
    else:
        form = TodoUpdateForm(instance=todo)
    return render(request, 'update.html', {'form':form})

def create(request):
    if request.method == 'POST':
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Todo.objects.create(title=data['title'], body=data['body'], created=data['created'])
            messages.success(request, 'Todo created successfully', 'success')
            return redirect('Todos')
    else:
        form = TodoCreateForm()
    return render(request, 'create.html', {'form':form})