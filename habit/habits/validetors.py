from rest_framework.serializers import ValidationError

from habits.models import Habit


class HabitWithoutReward:
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        tempval1 = dict(value).get(self.field1)
        tempval2 = dict(value).get(self.field2)
        if tempval1 and tempval2:
            raise ValidationError("Cannot select both a related habit and a reward.")


class HabitDuration:
    def __init__(self, field1):
        self.field1 = field1

    def __call__(self, value):
        tempval1 = dict(value).get(self.field1)
        if tempval1 > 120:
            raise ValidationError("Too long.")

class HabitReleted:
    def __init__(self, field1):
        self.field1 = field1

    def __call__(self, value):
        tempval1 = dict(value).get(self.field1)
        dicts_with_id = list(Habit.objects.filter(is_pleasurable=False).values())
        for i in dicts_with_id:
            if tempval1 is not None:
                if i['id'] == tempval1.id:
                    raise ValidationError("Habits must be pleasure")


class HabitWithoutRewardRelated:
    def __init__(self, field1, field2, field3):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3


    def __call__(self, value):
        tempval1 = dict(value).get(self.field1)
        tempval2 = dict(value).get(self.field2)
        tempval3 = dict(value).get(self.field3)
        if tempval1 == True and (tempval2 is not None or tempval3 is not None):
            raise ValidationError("Plesure habit can not have reward and related habit")

