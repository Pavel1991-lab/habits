
from rest_framework import serializers
from subscription.models import Subscription


class SubscriptionSerlizer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = '__all__'