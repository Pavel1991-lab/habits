from rest_framework import viewsets
from habits.models import Habit
from habits.serlizers import HabitsSerlizer
from rest_framework.permissions import IsAuthenticated
from django.utils.text import slugify


class HabitsViewSet(viewsets.ModelViewSet):
    serializer_class = HabitsSerlizer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        new_habits = serializer.save()
        new_habits.user = self.request.user
        new_habits.save()