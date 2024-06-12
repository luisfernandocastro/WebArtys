from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import *
from .models import *


# Create your views here.
def index_view(request):
    categorias = Categoria.objects.all()
    products = Producto.objects.all()
    return render(request, 'index.html',{
        'products': products,
        'categorias': categorias,
    })


# vistas de elusuario
def registro_view(request):

    if request.method == 'GET':
        return render(request, 'user/register.html',{
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'user/register.html',{
                    'form': UserCreationForm,
                    'error': 'Este usuario ya esta registrado'
                })
        return render(request, 'user/register.html',{
            'form': UserCreationForm,
            'error': 'Las contraseñas no coinciden'
        })

def cerrar_sesion(request):
    logout(request)
    return redirect('home')


def login_view(request):
    if request.method == 'GET':
        return render(request, 'user/login.html',{
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password= request.POST['password'])

        if user is None:
            return render(request, 'user/login.html',{
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrectos'
            })

        else:
            login(request, user)
            return redirect('home')



# vista para subir productos
@login_required 
def subir_producto(request):

    if request.method == 'POST':
        # request.FILES ,necesario para subir imagenes
        form = ProductForm(request.POST, request.FILES) # FILES sube la imagen seleccionada a la base de datos
        if form.is_valid(): # se valida si el formulario es correcto
            new_product = form.save(commit=False) # necesario para traer datos de otras instancias
            new_product.user = request.user # Le asigno al campo de usuario(user) la pk del usuario logueado 
            new_product.save() # se guarda el formulario
            messages.success(request, "producto subido correctamente") # mensaje a mostrar si la bicicleta se subio correctamente
            return redirect('home') # si el formulario es almacenado se muestra la ventana con el mensaje de exito [messages.success]
    else:# si el formulario no es por metodo POST se muestra el formulario vacio al hacer submit
        form = ProductForm()
        return render(request, 'user/subir_producto.html', {
            'form': form
        })
    


    # if request.method == 'GET':
    #     return render(request, 'user/subir_producto.html',{
    #         'form': ProductForm
    #     })
    # else:
    #     # try:
    #     form = ProductForm(request.POST, files=request.FILES )
    #     new_product = form.save(commit=False)
    #     new_product.user = request.user
    #     new_product.save()
    #     return redirect('homeUser')

        # except ValueError:
        #     return render(request, 'user/subir_producto.html',{
        #         'form': ProductForm,
        #         'error': 'Datos ingresados incorrectos'
        #     })