from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from user.models import CustomUser
from django.db import models

class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())

# class CodeForm(forms.ModelForm):
#     number = forms.CharField(label='Code', help_text='Tasdiqlash kodini kiriting...')
#     class Meta:
#         model = Code
#         fields = ['number']