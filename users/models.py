from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=100, id="email" ,unique=True)
    password = models.CharField(max_length=300, null=False)
    username = models.CharField(max_length=20, unique=True)
    gender = models.CharField(max_length=20)
    age = models.CharField(max_length=20)
    introduction = models.TextField(max_length=150)