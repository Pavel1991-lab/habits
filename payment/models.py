from django.db import models
from users.models import User


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_date = models.DateField()
    paid_course_or_lesson = models.CharField(max_length=100, choices=[('урок', 'lesson'), ('курс', 'course')])
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=100, choices=[('cash', 'Наличные'), ('transfer', 'Перевод на счет')])

