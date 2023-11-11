
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    name = models.CharField(unique=True, blank=True, null=True, verbose_name='имя')
    email = models.EmailField(unique=True, verbose_name='почта')
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name='аватарка')

    chat_id = models.CharField(max_length=255, blank=True, null=True, verbose_name='telegram chat id')

