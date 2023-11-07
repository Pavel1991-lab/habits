from rest_framework.serializers import ValidationError


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
