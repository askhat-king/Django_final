from django.contrib import admin

# Register your models here.
from .models import CreditCard, Order, ShoppingCart

admin.site.register(CreditCard)
admin.site.register(ShoppingCart)
admin.site.register(Order)
