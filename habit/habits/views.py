from rest_framework import viewsets, generics
from habits.models import Habit
from habits.serlizers import HabitsSerlizer
from rest_framework.permissions import IsAuthenticated
from django.utils.text import slugify

from habits.paginators import HabitsPaginator

from habits.permissions import IsOwner, CustomPermission


class HabitsViewSet(viewsets.ModelViewSet):
    serializer_class = HabitsSerlizer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
    pagination_class = HabitsPaginator

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_staff:
                return Habit.objects.all()  # администратор может видеть все привычки
            else:
                owned_habits = Habit.objects.filter(user=user)
                public_habits = Habit.objects.filter(is_public=True)
                return owned_habits | public_habits
        else:
            return None

    def perform_create(self, serializer):
        new_habits = serializer.save()
        new_habits.user = self.request.user
        new_habits.save()



# class PublicHabitListAPIView(generics.ListAPIView):
#     queryset = Habit.objects.filter(is_public=True)
#     permission_classes = [IsAuthenticated]
#     serializer_class = HabitsSerlizer
#     pagination_class = HabitsPaginator