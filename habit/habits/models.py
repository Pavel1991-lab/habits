from django.db import models



class Habit(models.Model):
    class Frequency(models.TextChoices):
        EACH_HOUR = 'each hour', 'каждый час'
        DAILY = 'daily', 'Раз в день'
        WEEKLY = 'weekly', 'Раз в неделю'
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, blank=True, null=True)
    place = models.CharField(max_length=100, blank=True, null=True)
    time = models.TimeField()
    action = models.CharField(max_length=100, blank=True, null=True)
    is_pleasurable = models.BooleanField(default=False)
    related_habit = models.ForeignKey('Habit', on_delete=models.SET_NULL, null=True, blank=True)
    frequency = models.CharField(
        max_length=50,
        choices=Frequency.choices,
        default=Frequency.WEEKLY)
    reward = models.CharField(max_length=100, blank=True, null=True)
    estimated_time = models.IntegerField()
    is_public = models.BooleanField(default=False, blank=True, null=True)
    habit_date = models.DateField()


    def __str__(self):
        return self.action
