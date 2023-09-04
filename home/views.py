from django.shortcuts import render
from .models import Todo

def sey_hello(request):
    person = {'name':'saleh'}
    return render(request, 'hello.html', context=person)

def home(request):
    return render(request, 'home.html')

def all_Todos(request):
    all = Todo.objects.all()
    return render(request, 'Todo.html', {'Todos':all})
