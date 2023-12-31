from django.db import models
from cart.models import Cart, CartItem
from authentication.models import CustomUser
from django.utils.crypto import get_random_string


# Create your models here.

class Order(models.Model):
    PENDING = 'pending'
    DELIVERED = 'delivered'
    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (DELIVERED, 'Delivered'),
    )
    order_id = models.CharField(max_length=12)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)

    def __str__(self) -> str:
        return self.order_id
    
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    cart_item = models.ForeignKey(CartItem, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.order.user.email
    
class OrderTrack(models.Model):
    order = models.OneToOneField(Order, on_delete=models.PROTECT)
    order_process = models.BooleanField(default=True)
    order_shipped = models.BooleanField(default=False)
    out_of_delivery = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.order.order_id