from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib import messages 
from django.contrib.auth import logout
from .forms import RegisterForm

from django.contrib.auth.models import User

from Tienda_online.models import Product

def holamundo(request):

    products = Product.objects.all().order_by('-id')

    return render(request,'index.html',{
        'message':'Mensaje desde la vista',
        'tilte':'Titulo',
        'products':products,
    })

def login_view(request):
    
    if request.user.is_authenticated:
            return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            messages.success(request,'¡Operación completada con éxito!')
            return redirect('home')
        else:
            messages.error(request, 'Acceso denegado')
        
    return render (request,"users/login.html")

def logout_view(request): 
    logout(request)
    messages.success(request, 'Session cerrada correctamente')
    return redirect('login')

def registro(request):
    if request.user.is_authenticated:
            return redirect('index')
     
    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        email= form.cleaned_data.get('email')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = User.objects.create_user(username,email,password)
        if user:
            login(request,user)
            messages.success(request,'Usuario creado existosamente')
            return redirect('home')

    return render(request, 'users/register.html',{
        'form': form
    })