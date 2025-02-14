from django.shortcuts import render
from models import Task

def addTask(request):
    if request.method == 'POST':
        nameTask = request.POST['nameTask']
        description = request.POST['description']
        dateCreation = request.POST['dateCreation']
        task = Task(nameTask=nameTask,description=description,dateCreation=dateCreation).save()
        
        return render(request, 'toDoListapp/cadastrar.html', {'task': task})