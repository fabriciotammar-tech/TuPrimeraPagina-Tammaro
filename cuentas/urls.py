from django.urls import path
from .views import login_view, registro_view, editar_perfil, acerca_de_mi
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name='login'),
    path('registro/', registro_view, name='registro'),
    path('logout/', LogoutView.as_view(template_name='cuentas/logout.html'), name='logout'),
    path('perfil/', editar_perfil, name='editar_perfil'),
    path('acerca-de-mi/', acerca_de_mi, name='acerca_de_mi'),
]