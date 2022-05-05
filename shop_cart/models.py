from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from auth_.models import MainUser
from main.models import Book, Comics, Item


# Create your models here.
class CreditCard(models.Model):
    number = models.CharField(max_length=16, blank=True)
    expireDate = models.CharField(max_length=50, blank=True)
    code = models.CharField(max_length=3, blank=True)
    customer = models.OneToOneField(MainUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Кредитная карта'
        verbose_name_plural = 'Кредитные карты'

    def __str__(self):
        return self.number


class ShoppingCart(models.Model):
    cart_items = models.ManyToManyField(Item)
    customer = models.ForeignKey(MainUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class Order(models.Model):
    price = models.FloatField()
    delivery_address = models.CharField(max_length=255)
    customer = models.ForeignKey(MainUser, on_delete=models.CASCADE)
    cart_items = models.ManyToManyField(ShoppingCart)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
