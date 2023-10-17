from django.shortcuts import render
from rest_framework import generics

from lesson.models import Lesson
from lesson.serlizers import LessonSerlizer


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerlizer

class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerlizer
    queryset = Lesson.objects.all()

class LessonRetrivAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerlizer
    queryset = Lesson.objects.all()

class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerlizer
    queryset = Lesson.objects.all()

class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
