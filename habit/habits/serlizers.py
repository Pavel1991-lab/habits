from rest_framework import serializers
from habits.models import Habit
from habits.validetors import HabitWithoutReward, HabitDuration, HabitReleted, HabitWithoutRewardRelated


class HabitsSerlizer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [HabitWithoutReward(field1='reward', field2='related_habit'),
                      HabitDuration(field1='estimated_time'),
                      HabitReleted(field1='related_habit'),
                      HabitWithoutRewardRelated(field1='is_pleasurable', field2='reward', field3='related_habit')]
