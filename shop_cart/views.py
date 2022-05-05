from django.shortcuts import render
import logging
from django.http import Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from main.models import Item
from main.serializers import ItemSerializer
from .models import CreditCard, ShoppingCart, Order
from .serializers import CreditCardSerializer, ShoppingCartSerializer, \
    OrderSerializer
from django.shortcuts import get_object_or_404, get_list_or_404

# Create your views here.

@csrf_exempt
def credit_card(request):
    if request.method == 'GET':
        credit_cards = CreditCard.objects.all()
        serializer = CreditCardSerializer(credit_cards, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        json_data = JSONParser().parse(request)
        serializer = CreditCardSerializer(data=json_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(serializer.errors, safe=False)


class CreditCardAPIView(APIView):
    permission_classes = (AllowAny, )

    def get_object(self, pk):
        try:
            return CreditCard.objects.get(pk=pk)
        except CreditCard.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        card = self.get_object(pk)
        serializer = CreditCardSerializer(card, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        card = self.get_object(pk)
        card.delete()
        logger.debug(f'CreditCard object deleted')
        logger.info(f'CreditCard object deleted')
        return Response(status=status.HTTP_204_NO_CONTENT)


class ShoppingCartAPIView(APIView):
    permission_classes = (AllowAny, )

    def get_object(self, pk):
        try:
            return ShoppingCart.objects.get(customer_id=pk)
        except ShoppingCart.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        shopping_cart = self.get_object(pk)
        serializer = ShoppingCartSerializer(shopping_cart)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        shopping_cart = self.get_object(pk)
        serializer = ShoppingCartSerializer(shopping_cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        shopping_cart = self.get_object(pk)
        shopping_cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def shopping_cart(request):
    if request.method == 'GET':
        shopping_cart = ShoppingCart.objects.all()
        serializer = ShoppingCartSerializer(shopping_cart, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        json_data = JSONParser().parse(request)
        serializer = ShoppingCartSerializer(data=json_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(serializer.errors, safe=False)


class OrderAPIView(APIView):
    permission_classes = (AllowAny, )

    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        order = self.get_object(pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        order= self.get_object(pk)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        order = self.get_object(pk)
        order.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def orders(request):
    if request.method == 'GET':
        all_orders = Order.objects.all()
        serializer = OrderSerializer(all_orders, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        json_data = JSONParser().parse(request)
        serializer = OrderSerializer(data=json_data)
        if serializer.is_valid():
            serializer.save()
            logger.debug(f'Order object created, ID: {serializer.instance}')
            logger.info(f'Order object created, ID: {serializer.instance}')
            return JsonResponse(serializer.data, safe=False)
        else:
            logger.error(f'Order object cannot be created, {serializer.errors}')
            return JsonResponse(serializer.errors, safe=False)
