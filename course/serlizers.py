from rest_framework import serializers

from course.models import Course
from lesson.serlizers import LessonSerlizer




class CourseSerlizer(serializers.ModelSerializer):

    all_lessons = serializers.IntegerField(read_only=True, source='lesson_set.all.count')
    lessons = LessonSerlizer(source='lesson_set', many=True, read_only=True)
    class Meta:
        model = Course
        fields = '__all__'