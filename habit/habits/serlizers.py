from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from habits.models import Habit
from users.models import User


class HabitsSerlizer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Habit
        fields = '__all__'