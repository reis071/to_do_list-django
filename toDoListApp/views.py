from django.shortcuts import render,redirect
from django.db.models import Q
from .models import Task

def addTask(request):
    if request.method == 'POST':
        nameTask = request.POST.get('nameTask')
        description = request.POST.get('description')
        

        if nameTask and description:  
            Task.objects.create(nameTask=nameTask, description=description)  
            return redirect('registerTask')
    return render(request, 'toDoListapp/registerTask.html')

    
def viewTasks(request):
    tasks = Task.objects.all()
    return render(request, 'toDoListapp/viewTasks.html', {'tasks': tasks})