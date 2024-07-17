from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User

class userRegisterForms(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Nombre"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Correo"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Contraseña"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Confirmar Contraseña"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Correo"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Contraseña"}))
