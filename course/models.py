from django.conf import settings
from django.db import models



class Course(models.Model):
    title = models.CharField(max_length=15, verbose_name='название')
    photo = models.ImageField(upload_to='photo/', blank=True, null=True, verbose_name='превью')
    description = models.TextField(verbose_name='описание')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, blank=True, null=True, verbose_name='user', related_name='course')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'
