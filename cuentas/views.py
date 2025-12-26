from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import MiRegistroForm
from .models import Avatar
from .forms import MiRegistroForm, UserEditForm

def registro_view(request):
    if request.method == "POST":
        form = MiRegistroForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
           
            if request.FILES.get("imagen"):
                Avatar.objects.create(user=user, imagen=request.FILES["imagen"])
            login(request, user)
            return redirect("home") 
    else:
        form = MiRegistroForm()
    return render(request, "cuentas/registro.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            clave = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "cuentas/login.html", {"form": form})

from django.contrib.auth.decorators import login_required
from .forms import UserEditForm # Asegúrate de crear este form en forms.py

@login_required
def editar_perfil(request):
    usuario = request.user
    # Intentamos obtener el avatar actual si existe
    try:
        avatar = usuario.avatar
    except Avatar.DoesNotExist:
        avatar = None

    if request.method == 'POST':
        form = UserEditForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            if request.FILES.get('imagen'):
                if avatar:
                    avatar.imagen = request.FILES['imagen']
                    avatar.save()
                else:
                    Avatar.objects.create(user=usuario, imagen=request.FILES['imagen'])
            form.save()
            return redirect('home')
    else:
        form = UserEditForm(instance=usuario)
    
    return render(request, 'cuentas/editar_perfil.html', {'form': form})

def acerca_de_mi(request):
    return render(request, 'entidades/acerca_de_mi.html')