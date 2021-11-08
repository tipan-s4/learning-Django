from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from . import forms
from .models import Profile
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

# Registramos al usuario
def signup_view(request):
    # Dependiendo del metodo que se use se realiza una accion o otra
    if request.method == 'POST':            
        # Si el metodo es post crearemos el usuario
        # Usamos los modelos de django para la verificacion y creacion de usuarios
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/')
    if request.method == 'GET':
        # Si el metodo es get mostraremos el formulario para registrarse
        form = UserCreationForm()
    return render(request,'accounts/signup.html',{'form':form})


#Iniciamos sesion
def login_view(request):
    if request.method == 'POST':            
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/')
    if request.method == 'GET':
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})


#Cerramos sesion 
def logout_view(request):  
    logout(request)
    return redirect('/')


# Borramos usuario
@login_required(login_url="/accounts/login/")
def delete_view(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        return redirect('/')
    else:
        return render(request,'accounts/delete.html')


# Perfil de usuario
@login_required(login_url="/accounts/login/")
def profile_view(request):
    # profile = Profile.objects.get(username=request.user)
    profile = Profile.objects.all().filter(username=request.user) 
    if profile:
        return render(request,'accounts/profile.html',{'profile':profile})
    else:
        if request.method == 'POST':
            form = forms.CreateProfile(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.username = request.user
                instance.save()
                return redirect('/')            
        else:
            form = forms.CreateProfile()
        return render(request,'accounts/profile.html',{'form':form})

# Editar usuario
@login_required(login_url="/accounts/login/")
def edit_view(request):
    profile = get_object_or_404(Profile,username=request.user)
    if request.method == 'POST':
        form = forms.CreateProfile(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save()
            return redirect('/accounts/profile/')
    else:
        form = forms.CreateProfile()
    return render(request,'accounts/edit.html',{'form':form})