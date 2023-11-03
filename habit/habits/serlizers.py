from rest_framework import serializers
from habits.models import Habit


class HabitsSerlizer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Habit
        fields = '__all__'