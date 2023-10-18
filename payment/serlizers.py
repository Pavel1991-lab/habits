from rest_framework import serializers
from payment.models import Payment

class PaymentSerlizer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'