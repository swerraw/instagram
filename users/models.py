from django.contrib.auth.models import  AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True,null=True,blank=True)
    avatar = models.ImageField(upload_to='avatars/',null=True,blank=True)
    bio = models.TextField(null=True,blank=True)
    links = models.TextField(null=True,blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

