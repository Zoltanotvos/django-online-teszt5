from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput, EmailInput

class Felhasználókészítés(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "password1"]

class Bejelentkezőformula(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())