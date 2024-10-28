from rest_framework import serializers
from django.core.exceptions import ValidationError
from .models import Items, Order





class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'
	

		
	
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['items', 'order_date', 'ordered', 'total_price']
       



