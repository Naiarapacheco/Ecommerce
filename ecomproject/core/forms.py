from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CadastroForm(UserCreationForm):
    primeiro_nome = forms.CharField(max_length=50, required=True)
    sobrenome = forms.CharField(max_length=50, required=True)
    email = forms.CharField(max_length=255, required=True)

    class Meta:
        model = User
        fields = ['username', 'primeiro_nome', 'sobrenome', 'email', 'password1', 'password2',]