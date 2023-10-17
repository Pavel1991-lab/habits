from django.conf import settings
from django.db import models



class Lesson(models.Model):
    title = models.CharField(max_length=15, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    photo = models.ImageField(upload_to='photo/', blank=True, null=True, verbose_name='превью')
    video_link = models.URLField(blank=True, null=True, verbose_name='видео')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
