
from rest_framework import viewsets
from course.models import Course
from course.serlizers import CourseSerlizer
from users.permissions import IsOwnerOrStaff
from course.paginators import CoursePaginator
from tasks import send_course_update_notification

class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerlizer
    queryset = Course.objects.all()
    permission_classes = [IsOwnerOrStaff]
    pagination_class = CoursePaginator

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.user = self.request.user
        new_course.save()

    def perform_update(self, serializer):
        updated_course = serializer.save()
        send_course_update_notification.delay(updated_course.id)



