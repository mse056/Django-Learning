from django.shortcuts import render

def sey_hello(request):
    person = {'name':'saleh'}
    return render(request, 'hello.html', context=person)

def home(request):
    return render(request, 'home.html')