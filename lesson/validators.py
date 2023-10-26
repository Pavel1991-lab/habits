
import re

from rest_framework.serializers import ValidationError



class LessonValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg = re.compile('https?://(www\.)?youtube\.com')
        tnp_val = dict(value).get(self.field)
        if not bool(reg.match(tnp_val)):
            raise ValidationError('Only YouTube links are allowed.')