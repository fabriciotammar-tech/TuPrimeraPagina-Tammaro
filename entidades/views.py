from django.shortcuts import render, redirect 
from .models import Bicicleta, Fabricante, Cliente, Venta 
from .forms import FabricanteForm, BicicletaForm, ClienteForm, VentaForm 
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# --- HOME ---
def home(request):
    return render(request, "entidades/index.html")

# --- LISTADOS ---
def lista_bicicletas(request):
    bicicletas = Bicicleta.objects.all()
    return render(request, "entidades/lista_bicicletas.html", {'bicicletas': bicicletas})

def lista_fabricantes(request):
    fabricantes = Fabricante.objects.all()
    return render(request, "entidades/lista_fabricantes.html", {'fabricantes': fabricantes})

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, "entidades/lista_clientes.html", {'clientes': clientes})

def lista_ventas(request):
    ventas = Venta.objects.all()
    return render(request, "entidades/lista_ventas.html", {'ventas': ventas})

# --- ALTAS (Solo logueados) ---
@login_required
def fabricante_alta(request):
    if request.method == 'POST':
        form = FabricanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_fabricantes') 
    else:
        form = FabricanteForm()
    return render(request, 'entidades/fabricante_form.html', {'form': form, 'titulo': 'Alta de Fabricante'})

@login_required
def bicicleta_alta(request):
    if request.method == "POST":
        form = BicicletaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_bicicletas')
    else:
        form = BicicletaForm()
    return render(request, 'entidades/bicicleta_form.html', {'form': form, 'titulo': 'Alta de Bicicleta'})

@login_required
def cliente_alta(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes') 
    else:
        form = ClienteForm()
    return render(request, 'entidades/cliente_form.html', {'form': form, 'titulo': 'Alta de Cliente'})

@login_required
def venta_alta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_ventas')
    else:
        form = VentaForm()
    return render(request, 'entidades/venta_form.html', {'form': form, 'titulo': 'Alta de Venta'})

# --- BÚSQUEDAS ---
def bicicleta_buscar(request):
    if request.GET.get("buscar"):
        patron = request.GET['buscar']
        bicicletas = Bicicleta.objects.filter(Q(modelo__icontains=patron) | Q(fabricante__nombre__icontains=patron))
    else:
        bicicletas = Bicicleta.objects.all()
    return render(request, 'entidades/bicicleta_buscar.html', {"bicicletas": bicicletas, "patron": request.GET.get("buscar", "")})

def fabricante_buscar(request):
    if request.GET.get("buscar"):
        patron = request.GET['buscar']
        fabricantes = Fabricante.objects.filter(nombre__icontains=patron)
    else:
        fabricantes = Fabricante.objects.all()
    return render(request, 'entidades/fabricante_buscar.html', {"fabricantes": fabricantes, "patron": request.GET.get("buscar", "")})

def cliente_buscar(request):
    if request.GET.get("buscar"):
        patron = request.GET['buscar']
        clientes = Cliente.objects.filter(Q(nombre__icontains=patron) | Q(apellido__icontains=patron))
    else:
        clientes = Cliente.objects.all()
    return render(request, 'entidades/cliente_buscar.html', {"clientes": clientes, "patron": request.GET.get("buscar", "")})

def venta_buscar(request):
    if request.GET.get("buscar"):
        patron = request.GET['buscar']
        ventas = Venta.objects.filter(Q(cliente__nombre__icontains=patron) | Q(bicicleta__modelo__icontains=patron))
    else:
        ventas = Venta.objects.all()
    return render(request, 'entidades/venta_buscar.html', {"ventas": ventas, "patron": request.GET.get("buscar", "")})

# --- EDITAR Y BORRAR ---

@login_required
def fabricante_editar(request, id_fabricante):
    fabricante = Fabricante.objects.get(id=id_fabricante)
    if request.method == "POST":
        form = FabricanteForm(request.POST, instance=fabricante)
        if form.is_valid():
            form.save()
            return redirect('lista_fabricantes')
    else:
        form = FabricanteForm(instance=fabricante)
    return render(request, 'entidades/fabricante_form.html', {'form': form, 'titulo': 'Editar Fabricante'})

@login_required
def fabricante_borrar(request, id_fabricante):
    fabricante = Fabricante.objects.get(id=id_fabricante)
    fabricante.delete()
    return redirect('lista_fabricantes')

@login_required
def bicicleta_editar(request, id_bici):
    bicicleta = Bicicleta.objects.get(id=id_bici)
    if request.method == "POST":
        form = BicicletaForm(request.POST, request.FILES, instance=bicicleta)
        if form.is_valid():
            form.save()
            return redirect('lista_bicicletas')
    else:
        form = BicicletaForm(instance=bicicleta)
    return render(request, 'entidades/bicicleta_form.html', {'form': form, 'titulo': 'Editar Bicicleta'})

@login_required
def bicicleta_borrar(request, id_bici):
    bicicleta = Bicicleta.objects.get(id=id_bici)
    bicicleta.delete()
    return redirect('lista_bicicletas')

@login_required
def cliente_editar(request, id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'entidades/cliente_form.html', {'form': form, 'titulo': 'Editar Cliente'})

@login_required
def cliente_borrar(request, id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    cliente.delete()
    return redirect('lista_clientes')

@login_required
def venta_editar(request, id_venta):
    venta = Venta.objects.get(id=id_venta)
    if request.method == "POST":
        form = VentaForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            return redirect('lista_ventas')
    else:
        form = VentaForm(instance=venta)
    return render(request, 'entidades/venta_form.html', {'form': form, 'titulo': 'Editar Venta'})

@login_required
def venta_borrar(request, id_venta):
    venta = Venta.objects.get(id=id_venta)
    venta.delete()
    return redirect('lista_ventas')