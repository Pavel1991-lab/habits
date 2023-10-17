from rest_framework import serializers

from lesson.models import Lesson


class LessonSerlizer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'