from django.shortcuts import render

def sey_hello(request):
    return render(request, 'hello.html')

def home(request):
    return render(request, 'home.html')