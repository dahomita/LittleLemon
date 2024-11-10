from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from .models import MenuItem, Order, OrderItem
from .serializers import (MenuItemSerializer, OrderSerializer, OrderItemSerializer,)

class UserViewSet(viewsets.ModelViewSet): 
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] 
  # Allow GET for all, edit for authenticated users


# Order Viewset
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self): 
        user = self.request.user
        return Order.objects.filter(user=user) #fiter
    
    @api_view()
    def assign_delivery_crew(self, request, pk=None): 
        order = self.get_object()
        return Response({'message': 'Delivery crew assigned'})
    
class OrderItemViewSet(viewsets.ModelViewSet): 
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated] 
  # Only authenticated users can manage order items

    def get_queryset(self):
        user = self.request.user
        return OrderItem.objects.filter(order__user=user)  # Filter based on authenticated user's orders

    