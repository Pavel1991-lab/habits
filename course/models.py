

from django.conf import settings
from django.db import models

from django.utils import timezone


class Course(models.Model):
    title = models.CharField(max_length=15, verbose_name='название')
    photo = models.ImageField(upload_to='photo/', blank=True, null=True, verbose_name='превью')
    description = models.TextField(verbose_name='описание')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, blank=True, null=True, verbose_name='user', related_name='course')
    modified_at = models.DateTimeField(auto_now=True, verbose_name='дата последнего обновления')
    previous_modified_at = models.DateTimeField(null=True, blank=True, verbose_name='предыдущая дата обновления')



    def save(self, *args, **kwargs):
        self.modified_at = timezone.now()
        if self.pk:  # Если экземпляр уже существует в базе данных
            previous_instance = Course.objects.get(pk=self.pk)  # Получаем предыдущий экземпляр из базы данных
            self.previous_modified_at = previous_instance.modified_at  # Устанавливаем previous_modified_at текущего экземпляра
        super(Course, self).save(*args, **kwargs)  # Вызываем сохранение родительского класса
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'



