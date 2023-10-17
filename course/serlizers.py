from rest_framework import serializers

from course.models import Course


class CourseSerlizer(serializers.ModelSerializer):

    all_lessons = serializers.IntegerField(read_only=True, source='lesson_set.all.count')

    class Meta:
        model = Course
        fields = '__all__'