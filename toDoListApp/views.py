from django.shortcuts import render

def home(request):
    return render(request, 'toDoListApp/index.html')

def sobre(request):
    return render(request, 'toDoListApp/teste.html')