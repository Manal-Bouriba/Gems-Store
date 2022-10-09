from django.db import models
from django.conf import settings
from decimal import Decimal

from django.db.models.fields import related
from store.models import Product
# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name='order_user')
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    order_key = models.CharField(max_length=200)
    billing_status = models.BooleanField(default= False)
    class Meta:
        ordering = ('created',)

    def __str__(self):
        return str(self.created)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return str(self.id)