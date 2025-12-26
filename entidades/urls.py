from django.urls import path
from . import views

urlpatterns = [
 
    path('', views.home, name='home'),
    path('bicicletas/', views.lista_bicicletas, name='lista_bicicletas'),
    path('fabricantes/', views.lista_fabricantes, name='lista_fabricantes'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('ventas/', views.lista_ventas, name='lista_ventas'),
    
   
    path('fabricante_alta/', views.fabricante_alta, name='fabricante_alta'),
    path('bicicleta_alta/', views.bicicleta_alta, name='bicicleta_alta'),
    path('cliente_alta/', views.cliente_alta, name='cliente_alta'),
    path('venta_alta/', views.venta_alta, name='venta_alta'),

  
    path('fabricante_buscar/', views.fabricante_buscar, name='fabricante_buscar'),
    path('bicicleta_buscar/', views.bicicleta_buscar, name='bicicleta_buscar'),
    path('cliente_buscar/', views.cliente_buscar, name='cliente_buscar'),
    path('venta_buscar/', views.venta_buscar, name='venta_buscar'),

   
    path('fabricante_editar/<int:id_fabricante>/', views.fabricante_editar, name='fabricante_editar'),
    path('fabricante_borrar/<int:id_fabricante>/', views.fabricante_borrar, name='fabricante_borrar'),

    path('bicicleta_editar/<int:id_bici>/', views.bicicleta_editar, name='bicicleta_editar'),
    path('bicicleta_borrar/<int:id_bici>/', views.bicicleta_borrar, name='bicicleta_borrar'),

    path('cliente_editar/<int:id_cliente>/', views.cliente_editar, name='cliente_editar'),
    path('cliente_borrar/<int:id_cliente>/', views.cliente_borrar, name='cliente_borrar'),

    path('venta_editar/<int:id_venta>/', views.venta_editar, name='venta_editar'),
    path('venta_borrar/<int:id_venta>/', views.venta_borrar, name='venta_borrar'),
]