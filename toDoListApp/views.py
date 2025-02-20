from django.shortcuts import render,redirect
from .models import Task

def addTask(request):
    if request.method == 'POST':
        nameTask = request.POST.get('nameTask')
        description = request.POST.get('description')
        dateCreation = request.POST.get('dateCreation')

        if nameTask and description and dateCreation:  # Verifica se os campos não estão vazios
            Task.objects.create(nameTask=nameTask, description=description, dateCreation=dateCreation)  

    return render(request, 'toDoListapp/registerTask.html')