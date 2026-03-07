from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# Таблиці в БД
class CustomUser(AbstractUser):
    image_small = models.ImageField(upload_to='avatars/', null=True, blank=True)
    image_medium = models.ImageField(upload_to='avatars/', null=True, blank=True)
    image_large = models.ImageField(upload_to='avatars/', null=True, blank=True)
    
    def __str__(self):
        return self.email