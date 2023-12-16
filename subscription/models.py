
from django.db import models

from course.models import Course


class Subscription(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='user', blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name='подписка')

    def __str__(self):
        return self.is_active

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'