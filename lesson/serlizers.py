from rest_framework import serializers
from lesson.models import Lesson
from lesson.validators import LessonValidator


class LessonSerlizer(serializers.ModelSerializer):



    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [LessonValidator(field='video_link')]