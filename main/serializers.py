from rest_framework import serializers
from main.models import Book, Comics, Publisher, SimilarComics, SimilarBook, Author, Item


class PublisherSerializer(serializers.Serializer):
    name = serializers.CharField()
    address = serializers.CharField()
    city = serializers.CharField()
    country = serializers.CharField()

    def create(self, validated_data):
        publisher = Publisher.objects.create(name=validated_data.get('name'), address=validated_data.get('address'),
                                             city=validated_data.get('city'), country=validated_data.get('country'))
        return publisher

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('name', 'price', 'genre', 'image', 'type', 'num_pages',)

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError('price must be positive')
        return value

    def validate_num_pages(self, value):
        if value < 1:
            raise serializers.ValidationError('page number must be positive')
        return value

    # def validate(self, attrs):
    #     return attrs


class ComicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comics
        fields = ('name', 'price', 'genre', 'image', 'color_type', 'release_type',)

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError('price must be positive')
        return value


class AuthorSerializer(serializers.ModelSerializer):
    book = BookSerializer

    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'book', 'comics')


class AuthorretrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name')


class BookFullSerializer(BookSerializer):
    authors = AuthorretrieveSerializer(many=True)

    publisher = PublisherSerializer()

    class Meta(BookSerializer.Meta):
        fields = BookSerializer.Meta.fields + ('authors', 'publisher')

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError('price must be positive')
        return value


class ComicsFullSerializer(ComicsSerializer):
    authors = AuthorretrieveSerializer(many=True)
    publisher = PublisherSerializer()

    class Meta(ComicsSerializer.Meta):
        fields = ComicsSerializer.Meta.fields + ('authors', 'publisher')

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError('price must be positive')
        return value


class SimilarBookSerializer(serializers.Serializer):
    name = serializers.CharField()
    book = serializers.PrimaryKeyRelatedField

    def create(self, validated_data):
        book = SimilarBook.objects.create(name=validated_data.get('name'), book=validated_data.get('book'))
        return book

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.book = validated_data.get('book', instance.book)
        instance.save()
        return instance


class SimilarComicsSerializer(serializers.Serializer):
    name = serializers.CharField()
    comics = serializers.PrimaryKeyRelatedField

    def create(self, validated_data):
        comics = SimilarComics.objects.create(name=validated_data.get('name'), comics=validated_data.get('comics'))
        return comics

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.comics = validated_data.get('comics', instance.comics)
        instance.save()
        return instance


class ItemSerializer(serializers.Serializer):
    item_name = serializers.CharField()
    price = serializers.FloatField()
    weight = serializers.CharField()
    from_where = serializers.CharField()
    description = serializers.CharField()
    photo = serializers.ImageField()

    def create(self, validated_data):
        category = Category.objects.get(id=validated_data.get('category'))
        Item = Item.objects.create(item_name=validated_data.get('item_name'),
                                   price=validated_data.get('price'),
                                   weight=validated_data.get('weight'),
                                   from_where=validated_data.get('from_where'),
                                   description=validated_data.get('description'),
                                   photo=validated_data.get('photo'))
        return Item

    def update(self, instance, validated_data):
        instance.item_name = validated_data.get('item_name', instance.item_name)
        instance.price = validated_data.get('price', instance.price)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.from_where = validated_data.get('from_where', instance.from_where)
        instance.description = validated_data.get('description', instance.description)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.save()
        return instance

    def validate(self, data):
        if data['price'] <= 0:
            raise serializers.ValidationError("Price can't be negative number or zero!")
        return data
