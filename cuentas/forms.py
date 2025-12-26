from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MiRegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    imagen = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ("username", "email", "imagen")
class UserEditForm(forms.ModelForm):
    imagen = forms.ImageField(required=False)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']