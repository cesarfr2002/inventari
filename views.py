
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate

def login_view(request):
    if request.method == 'POST':
        if 'email' in request.POST:  # Registration form
            username = request.POST['email']
            password = request.POST['password']
            name = request.POST['nombre']
            
            if User.objects.filter(username=username).exists():
                messages.error(request, 'El usuario ya existe')
                return redirect('login')
            
            try:
                user = User.objects.create_user(
                    username=username,
                    email=username,
                    password=password,
                    first_name=name
                )
                user = authenticate(username=username, password=password)
                if user:
                    login(request, user)
                    return redirect('list_clients')
                messages.success(request, 'Usuario creado exitosamente')
                return redirect('login')
            except Exception as e:
                messages.error(request, f'Error al crear usuario: {str(e)}')
                return redirect('login')
        else:  # Login form
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('list_clients')
            else:
                messages.error(request, 'Credenciales inválidas')
    
    return render(request, 'login.html')