from django.contrib import admin
from django.urls import path
from app.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(), name='login'),
    path('home/', Home.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', Logout.as_view(), name='logout'),
    path('female/', Female.as_view(), name='female'),
]
