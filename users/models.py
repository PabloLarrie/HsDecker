from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    username = models.CharField(max_length=15)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=50)
    bio = models.TextField(max_length=250)
    avatar = models.ImageField()
