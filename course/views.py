from django.shortcuts import render
from rest_framework import viewsets
from course.models import Course
from course.serlizers import CourseSerlizer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerlizer
    queryset = Course.objects.all()



