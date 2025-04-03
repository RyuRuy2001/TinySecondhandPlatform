from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'image', 'category']

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=15, label='아이디')
    password1 = forms.CharField(label='비밀번호', widget=forms.PasswordInput, max_length=15)
    password2 = forms.CharField(label='비밀번호 확인', widget=forms.PasswordInput, max_length=15)

    class Meta:
        model = User
        fields = ("username",)
