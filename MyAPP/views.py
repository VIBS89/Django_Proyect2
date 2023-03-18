from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# Modelo de usuario que trae por defecto Django el cual nos permite registrar nuestros usuarios por medio de la clase / libreria user
from django.contrib.auth.models import User
from django.http import HttpResponse
# Importamos login que nos permitira autenticar el usuario y generar cookies
from django.contrib.auth import login

# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # Registrar el usuario
            # Validamos con un Try..Except para evitar cualquier posible error en App y a nivel BD y asi poderlo capturar
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                """ return render(request,'signup.html',{
                    'form': UserCreationForm,
                    'error':'Usuario Creado Satisfactoriamente'
                }) """
                login(request, user)
                return redirect('tasks')
            except:
                return render(request,'signup.html',{
                    'form': UserCreationForm,
                    'error':'El Usuario Ya Existe'
                })
    return render(request,'signup.html',{
                    'form': UserCreationForm,
                    'error':'El Password No Tiene Coincidencia'
                })

def tasks(request):
    return render(request, 'tasks.html')