from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *

class SignUpForm(UserCreationForm):   
    # first_name = forms.CharField(max_length=30, required=True)
    # last_name = forms.CharField(max_length=30, required=True)
    # username = forms.CharField(max_length=30, required=True)
    
    class Meta:
        model = SignUpCustom
        fields = ('username','first_name', 'last_name', 'phone', 'gender', 'password1', 'password2')
        # fields = UserCreationForm.Meta.fields + ('phone', 'gender')