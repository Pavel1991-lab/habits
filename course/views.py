
from rest_framework import viewsets
from course.models import Course
from course.serlizers import CourseSerlizer
from users.permissions import IsOwnerOrStaff
from course.paginators import CoursePaginator


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerlizer
    queryset = Course.objects.all()
    permission_classes = [IsOwnerOrStaff]
    pagination_class = CoursePaginator



