from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    bio = models.TextField(blank=True)
    region = models.CharField(max_length=100, blank=True)
