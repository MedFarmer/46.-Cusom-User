from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import FormMixin
from django.http import HttpResponseRedirect

class GenderMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.gender == 'female':
            return redirect('female')
        return super().dispatch(request, *args, **kwargs)

class Logout(LogoutView):
    next_page = 'login'
    
class Home(GenderMixin, TemplateView):
    template_name = 'home.html'

class SignUpView(CreateView):
    model = SignUpCustom
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
    
class LoginView(FormMixin, View):
    form_class = LoginForm()
    success_url = reverse_lazy('home')    
    
    def form_valid(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        return HttpResponseRedirect(self.success_url)   
        
    def post(self, request):
        response = self.form_valid(request)
        return response
        
    def get(self, request):
        form = LoginForm()
        context = {'form':form}
        return render(request, 'login.html', context)  
    
class Female(TemplateView):
    template_name = 'female.html'

class Logout(LogoutView):
    next_page = 'login'
