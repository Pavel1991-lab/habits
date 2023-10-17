from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=15, verbose_name='телефон')
    city = models.CharField(max_length=100, verbose_name='город')
    avatar = models.ImageField(upload_to='avatars/', verbose_name='аватарка')


