from django.shortcuts import render
from rest_framework import generics

from lesson.models import Lesson
from lesson.serlizers import LessonSerlizer
from rest_framework.permissions import IsAuthenticated

from users.permissions import IsOwnerOrStaff


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerlizer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.user = self.request.user
        new_lesson.save()




class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerlizer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwnerOrStaff]


class LessonRetrivAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerlizer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwnerOrStaff]



class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerlizer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwnerOrStaff]



class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsOwnerOrStaff]


