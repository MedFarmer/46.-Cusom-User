from django.db import models
from django.contrib.auth.models import AbstractUser

class SignUpCustom(AbstractUser):
    phone = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    
    def __str__(self):
        return self.first_name
