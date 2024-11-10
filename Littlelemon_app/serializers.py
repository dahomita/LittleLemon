from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import MenuItem, Order, OrderItem

class MenuItemSerializer(serializers.Serializer): 
    model = MenuItem 
    field = ('id', 'title', 'price', 'category')

class OrderSerializer(serializers.ModelSerializer): 
    user = serializers.CharField(read_only=True, source='user.username')
    order_items = serializers.SerializerMethodField()

    def get_order_items(self, obj): 
        items = OrderItem.objects.filter(order=obj)
        return MenuItemSerializer(items, many=True).data
    
    class Meta: 
        model = Order
        fields = ('id', 'user', 'created_at', 'order_items', 'status') #Add status field for order status

class OrderItemSerializer(serializers.ModelSerializer): 
    menu_item = MenuItemSerializer(read_only = True)

    class Meta: 
        model = OrderItem
        fields = ('id', 'order', 'menu_item', 'quantity')