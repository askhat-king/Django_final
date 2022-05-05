from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, filters
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from main.models import Book, Comics, Publisher, SimilarBook, SimilarComics, Item
from main.serializers import BookSerializer, ComicsSerializer, PublisherSerializer, SimilarBookSerializer, \
    SimilarComicsSerializer, BookFullSerializer, ComicsFullSerializer, ItemSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import action
import logging
logger = logging.getLogger(__name__)

# Create your views here.

class ComicsViewSet(viewsets.ModelViewSet):
    # permission_classes = (AllowAny,)
    queryset = Comics.objects.all()
    serializer_class = ComicsSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    filter_backends = (DjangoFilterBackend,
                       filters.SearchFilter,)
    search_fields = ('name', 'genre',)

    def get_permissions(self):
        logger.debug('get permissions')
        logger.info('get permissions')
        logger.warning('get permissions')
        logger.error('get permissions')
        logger.critical('get permissions')

        if self.action == 'list':
            permission_classes = (AllowAny,)
        else:
            permission_classes = (AllowAny,)

        return [permission() for permission in permission_classes]


class BookViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    filter_backends = (DjangoFilterBackend,
                       filters.SearchFilter,)
    search_fields = ('name', 'genre',)

    def get_permissions(self):
        logger.debug('get permissions')
        logger.info('get permissions')
        logger.warning('get permissions')
        logger.error('get permissions')
        logger.critical('get permissions')

        if self.action == 'list':
            permission_classes = (AllowAny,)
        else:
            permission_classes = (AllowAny,)

        return [permission() for permission in permission_classes]


class ComicsFullViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Comics.objects.all()
    serializer_class = ComicsFullSerializer

class BookFullViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Book.objects.all()
    serializer_class = BookFullSerializer


class PublisherListAPIView(generics.ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = (AllowAny,)

class PublisherDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = (AllowAny,)

class SimilarBookListAPIView(generics.ListCreateAPIView):
    queryset = SimilarBook.objects.all()
    serializer_class = SimilarBookSerializer
    permission_classes = (AllowAny,)

class SimilarBookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SimilarBook.objects.all()
    serializer_class = SimilarBookSerializer
    permission_classes = (AllowAny,)

class SimilarComicsListAPIView(generics.ListCreateAPIView):
    queryset = SimilarComics.objects.all()
    serializer_class = SimilarComicsSerializer
    permission_classes = (AllowAny,)


class SimilarComicsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SimilarComics.objects.all()
    serializer_class = SimilarComicsSerializer
    # serializer_class.is_valid(raise_exception=True)
    permission_classes = (AllowAny,)


class ItemViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny, )

    def list(self, request):
        queryset = Item.objects.all()
        serializer = ItemSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Item.objects.filter()
        user = get_list_or_404(queryset)
        serializer = ItemSerializer(user, many=True)
        return Response(serializer.data)

    @action(methods=['POST'], detail=False, permission_classes=(AllowAny,))
    def create(self, request):
        item_data = request.data
        new_item = Item.objects.create(item_name=item_data['item_name'], price=item_data['price'],
                                           weight=item_data['weight'], from_where=item_data['from_where'],
                                       description=item_data['description'],photo=item_data['photo'],)
        new_item.save()
        serializer = ItemSerializer(new_item)
        logger.debug(f'Item object created, ID: {serializer.instance}')
        logger.info(f'Item object created, ID: {serializer.instance}')
        return Response(serializer.data)

    def destroy(self, request, pk):
        try:
            instance = Item.objects.get(id=pk)
            instance.delete()
            logger.debug(f'Item object deleted, ID: {instance}')
            logger.info(f'Item object deleted, ID: {instance}')
        except Http404:
            logger.error(f'Item object cannot be deleted')
        return Response(status=status.HTTP_204_NO_CONTENT)

    def select(self, request, pk=None):
        queryset = Item.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = ItemSerializer(user)
        return Response(serializer.data)

    @action(methods=['PUT'], detail=False, permission_classes=(AllowAny, ))
    def update(self, request, pk):
        _item = Item.objects.get(id=pk)
        _item.item_name = request.data['item_name']
        _item.price = request.data['price']
        _item.weight = request.data['weight']
        _item.from_where = request.data['from_where']
        _item.description = request.data['description']
        _item.photo = request.data['photo']
        _item.save()
        serializer = ItemSerializer(_item)
        logger.debug(f'Item object updated, ID: {serializer.instance}')
        logger.info(f'Item object updated, ID: {serializer.instance}')
        return Response(serializer.data)
