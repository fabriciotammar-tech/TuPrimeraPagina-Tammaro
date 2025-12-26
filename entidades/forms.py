

from django import forms
from .models import Fabricante, Bicicleta, Cliente, Venta

class FabricanteForm(forms.ModelForm):
    class Meta:
        model = Fabricante
        fields = ['nombre', 'pais_origen']

class BicicletaForm(forms.ModelForm):
    class Meta:
        model = Bicicleta
        fields = ['modelo', 'descripcion_corta', 'fabricante', 'cuerpo', 'imagen', 'rodado', 'precio']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'email', 'telefono']

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['cliente', 'bicicleta', 'total']