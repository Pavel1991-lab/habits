
import re

from rest_framework.serializers import ValidationError



class LessonValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg = re.compile('https://youtube.com')
        tnp_val = dict(value).get(self.field)
        if tnp_val:
            if 'https://www.youtube.com/' not in tnp_val:
                raise ValidationError('Only youtube')

