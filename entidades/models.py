from django.db import models
from ckeditor.fields import RichTextField 

# 1. Modelo Fabricante
class Fabricante(models.Model):
    nombre = models.CharField(max_length=100)
    pais_origen = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# 2. Modelo Bicicleta 
class Bicicleta(models.Model):
    modelo = models.CharField(max_length=100) 
    descripcion_corta = models.CharField(max_length=200) 
    cuerpo = RichTextField(null=True, blank=True) 
    imagen = models.ImageField(upload_to='bicicletas/', null=True, blank=True)
    fecha_ingreso = models.DateField(auto_now_add=True)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE)
    rodado = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.modelo} - {self.fabricante}"

# 3. Modelo Cliente
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# 4. Modelo Venta
class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    bicicleta = models.ForeignKey(Bicicleta, on_delete=models.CASCADE)
    fecha_venta = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)