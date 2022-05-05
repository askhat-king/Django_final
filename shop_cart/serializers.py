from rest_framework import serializers
from .models import CreditCard, ShoppingCart, Order
#

class CreditCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = '__all__'

    def validate_number(self, value):
        if '-' in value:
            raise serializers.ValidationError('Invalid chars!')
        return value


class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
