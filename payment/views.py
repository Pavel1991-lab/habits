from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter

from payment.models import Payment
from payment.serlizers import PaymentSerlizer


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerlizer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]  # Бэкенд для обработки фильтра
    filterset_fields = ('paid_course_or_lesson', 'payment_method')
    ordering_fields = ('payment_date')
