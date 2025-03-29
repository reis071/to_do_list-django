from django.shortcuts import render,redirect
from .models import Task
from django.contrib.auth.decorators import login_required

@login_required
def addTask(request):
    if request.method == 'POST':
        nameTask = request.POST.get('nameTask')
        description = request.POST.get('description')
        

        if nameTask and description:  
            Task.objects.create(user=request.user, nameTask=nameTask, description=description)  
            return redirect('registerTask')
    return render(request, 'toDoListApp/registerTask.html')

    
@login_required
def viewTasks(request):
    
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'toDoListApp/viewTasks.html', {'tasks': tasks})

