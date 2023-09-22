from typing import Any
from django import forms

from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100, required=True,widget=forms.TextInput(attrs={
        'class':'form-control',
        'id':'username',
        'placeholder':'Agustin'
    }))
    password = forms.CharField(max_length=50, required=True,widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'id':'password',
    }))
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={
        'class':'form-control',
        'id':'email',
        'placeholder':'example@gmail.com'
    }))

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El username ya se encuentra en uso')

        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El correo ya se encuentra en uso')

        return email
    
    def save(self):
        return User.objects.create_user(
            self.cleaned_data.get('username'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password'),
        )