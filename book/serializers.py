from decimal import Decimal

from rest_framework import serializers

from book.models import Publisher, Book


class PublisherSerializer(serializers.ModelSerializer):
    number_of_books_published = serializers.IntegerField(read_only=True)
    class Meta:
        model = Publisher
        fields = ['id', 'name', 'email', 'website', 'number_of_books_published']
    # name = serializers.CharField(max_length=255)
    # email = serializers.EmailField()
    # website = serializers.URLField()


class BookSerializer(serializers.ModelSerializer):  # noqa
    id = serializers.IntegerField(read_only=True)
    discounted_price =serializers.SerializerMethodField(method_name="discount", read_only=True)

    def discount(self, book):
        return book.price * Decimal("0.8")

    # title = serializers.CharField(max_length=255)
    # isbn = serializers.CharField(max_length=255)
    # price = serializers.DecimalField(max_digits=6, decimal_places=2)
    # publisher = serializers.PrimaryKeyRelatedField(
    #     queryset=Publisher.objects.all()
    # )
    # publisher = serializers.HyperlinkedRelatedField(
    #     queryset=Publisher.objects.all(),
    #     view_name="book:publisher-detail"
    # )

    class Meta:
        model = Book
        # fields = "__all__"
        fields = ['id', 'title', 'isbn', 'genre', 'price', 'discounted_price', 'date_published', 'edition', 'publisher']
