from django.shortcuts import render,redirect
from django.contrib.auth import *

User = get_user_model()

# Create your views here.

def registerUser(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(email=email, password=password, name=name)
        return redirect('login')
    
    return render(request, 'userApp/register.html')

def loginUser(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return redirect('registerTask')  # redireciona para página de tarefas
        else:
            return render(request, 'userApp/login.html', {'erro': 'Credenciais inválidas'})

    return render(request, 'userApp/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')  