from django.shortcuts import render
from rest_framework import generics

from lesson.models import Lesson
from lesson.serlizers import LessonSerlizer
from rest_framework.permissions import IsAuthenticated, AllowAny

# from users.permissions import IsOwnerOrStaff
from tasks import  send_lesson_update_notification
from lesson.paginators import LessonPaginator


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerlizer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.user = self.request.user
        new_lesson.save()




class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerlizer
    queryset = Lesson.objects.all()
    permission_classes = [AllowAny]
    pagination_class = LessonPaginator


class LessonRetrivAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerlizer
    queryset = Lesson.objects.all()
    permission_classes = [AllowAny]



class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerlizer
    queryset = Lesson.objects.all()
    permission_classes = [AllowAny]

    def perform_update(self, serializer):
        lesson_id = serializer.save()
        send_lesson_update_notification.delay(lesson_id.id)


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [AllowAny]


