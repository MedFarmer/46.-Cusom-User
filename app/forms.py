from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *

class SignUpForm(UserCreationForm):    
       
    class Meta:
        model = SignUpCustom
        fields = ('username','first_name', 'last_name', 'phone', 'gender', 'password1', 'password2')
      

class LoginForm(forms.Form): 
      
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())