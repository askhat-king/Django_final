from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from .views import PublisherListAPIView, PublisherDetailAPIView, SimilarBookListAPIView,  SimilarComicsListAPIView, \
    BookViewSet, ComicsViewSet, SimilarBookDetailAPIView, SimilarComicsDetailAPIView, BookFullViewSet, \
    ComicsFullViewSet, ItemViewSet

router = DefaultRouter()
router.register(r'books', viewset=BookViewSet, basename='main')
router.register(r'comics', viewset=ComicsViewSet, basename='main')
router.register(r'comics/all', viewset=ComicsFullViewSet, basename='main')
router.register(r'books/all', viewset=BookFullViewSet, basename='main')

urlpatterns = [

path('publisher/', PublisherListAPIView.as_view()),
path('publisher/<int:pk>/', PublisherDetailAPIView.as_view()),

path('similar/book/',  SimilarBookListAPIView.as_view()),
path('similar/book/<int:pk>/', SimilarBookDetailAPIView.as_view()),

path('similar/comics/', SimilarComicsListAPIView.as_view()),
path('similar/comics/<int:pk>/', SimilarComicsDetailAPIView.as_view()),

path('items/', ItemViewSet.as_view({'get': 'list', 'post': 'create'})),
path('items/<int:pk>', ItemViewSet.as_view({'delete': 'destroy', 'get': 'select', 'put': 'update'})),

path('', include(router.urls)),
path('', include('shop_cart.urls')),
]