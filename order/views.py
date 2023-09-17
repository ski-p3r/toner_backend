from django.shortcuts import render, get_object_or_404
from rest_framework import generics, pagination, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import Order,OrderItem
from .serializers import  OrderSerializer, OrderItemSerializer

from django.utils.crypto import get_random_string
# Create your views here.

class OrderCreatListView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    pagination_class = pagination.PageNumberPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            order = Order.objects.filter(user=user)
            return order
        return Response({"response": "User must logged in"})
    
    def post(self, request, *args, **kwargs):
        user = self.request.user
        if user.is_authenticated:
            order = Order.objects.create(
                user=user,
                order_id=get_random_string(12).upper()
            )
            return Response(self.serializer_class(order).data, status=status.HTTP_201_CREATED)
        return {"response": "user must login"}

class OrderItemsListCreateView(generics.ListCreateAPIView):
    serializer_class = OrderItemSerializer
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        order=get_object_or_404(Order, pk=pk)
        try:
            order_items = OrderItem.objects.filter(order=order)
        except order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return order_items