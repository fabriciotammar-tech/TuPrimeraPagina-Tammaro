from django.contrib import admin
from .models import Fabricante, Bicicleta, Cliente, Venta

# --- 1. Fabricante Admin ---
@admin.register(Fabricante)
class FabricanteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais_origen') 
    search_fields = ('nombre', 'pais_origen')
    ordering = ('nombre',)

# --- 2. Bicicleta Admin ---
@admin.register(Bicicleta)
class BicicletaAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'precio', 'fabricante', 'fecha_ingreso') 
    list_filter = ('fabricante', 'fecha_ingreso') 
    ordering = ('modelo',) 
    search_fields = ('modelo', 'fabricante__nombre') 

# --- 3. Cliente Admin ---
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'telefono')
    search_fields = ('apellido', 'email')
    ordering = ('apellido',)

# --- 4. Venta Admin ---
@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'bicicleta', 'total', 'fecha_venta')
    list_filter = ('fecha_venta', 'cliente')
    ordering = ('-fecha_venta',)