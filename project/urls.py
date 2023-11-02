from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', Login.as_view(), name='login'),
    path('', Home.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),    
]
