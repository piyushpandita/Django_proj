from django import forms
from django.contrib.auth.models import User
from django.contrib import messages


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['email', 'username', 'password']


class LoginForm(forms.ModelForm):
    """docstring for RegisterForm"""
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password']

