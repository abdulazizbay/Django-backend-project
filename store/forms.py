from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth.models import User
from django.db import models

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2",)

class LoginForm(forms.Form):
    class Meta:
        username = forms.CharField(max_length=50)
        password = forms.CharField(max_length=50)