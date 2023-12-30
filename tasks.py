from datetime import datetime, timedelta, time
from time import timezone

from celery import shared_task
from django.core.mail import send_mail

from course.models import Course
from config import settings
from lesson.models import Lesson
from subscription.models import Subscription

@shared_task
def send_course_update_notification(course_id):
    course = Course.objects.filter(pk=course_id).get()
    print(course.id)
    current_time = datetime.now().time()
    if (course.modified_at + timedelta(hours=5)) <  current_time:
        subscribers = Subscription.objects.filter(course=course, is_active=True).get()
        print(subscribers.id)
        send_mail(
            'Обновление курса',
            f'Курс "{course.title}" был обновлен. Посетите страницу курса для получения более подробной информации.',
            settings.EMAIL_HOST_USER,
            [subscribers.user.email]
        )


@shared_task
def send_lesson_update_notification(lesson_id):
    lesson = Lesson.objects.filter(pk=lesson_id).get()
    course_id = lesson.course.id
    print(course_id)
    course = Course.objects.filter(pk=course_id).get()
    subscribers = Subscription.objects.filter(course=course, is_active=True).get()
    send_mail(
        'Обновление урока',
        f'Урок "{lesson.title}" был обновлен. Посетите страницу курса для получения более подробной информации.',
                 settings.EMAIL_HOST_USER,
        [subscribers.user.email]
    )