from rest_framework import serializers
from habits.models import Habit
from habits.validetors import HabitWithoutReward, HabitDuration, HabitReleted




class HabitsSerlizer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [HabitWithoutReward(field1='reward', field2='related_habit'), HabitDuration(field1='estimated_time'),
                      HabitReleted]