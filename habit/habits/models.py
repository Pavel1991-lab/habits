from django.db import models



class Habit(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, blank=True, null=True)
    place = models.CharField(max_length=100, blank=True, null=True)
    time = models.TimeField()
    action = models.CharField(max_length=100, blank=True, null=True)
    is_pleasurable = models.BooleanField(default=False)
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    frequency = models.IntegerField(default=1, blank=True, null=True)
    reward = models.CharField(max_length=100, blank=True, null=True)
    estimated_time = models.IntegerField()
    is_public = models.BooleanField(default=False, blank=True, null=True)



    def __str__(self):
        return self.action
