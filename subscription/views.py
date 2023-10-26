from rest_framework import viewsets
from subscription.models import Subscription
from subscription.serlizers import SubscriptionSerlizer

from users.permissions import IsOwnerOrStaff



class SubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = SubscriptionSerlizer
    queryset = Subscription.objects.all()

