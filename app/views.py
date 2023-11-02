from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *

# class Login(LoginView):
#     model = SignUpCustom
#     authetication_form = LoginForm
#     next_page = 'home'

class Logout(LogoutView):
    next_page = 'home'
    
class Home(TemplateView):
    template_name = 'home.html'

class SignUpView(CreateView):
    model = SignUpCustom
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = reverse_lazy('home')