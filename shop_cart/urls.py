from django.urls import path
from shop_cart import views


urlpatterns = [
    path('creditcards', views.credit_card),
    path('creditcards/<int:pk>', views.CreditCardAPIView.as_view()),
    path('shoppingcart/<int:pk>', views.ShoppingCartAPIView.as_view()),
    path('shoppingcart', views.shopping_cart),
    path('orders', views.orders),
    path('orders/<int:pk>', views.OrderAPIView.as_view()),
]