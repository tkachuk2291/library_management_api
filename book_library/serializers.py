from rest_framework import serializers

from book_library.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', "title" , "author" , "published_date" , "isbn" , "pages" , "cover" , "language")


class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', "title" , "author" , "published_date" , "isbn" , "pages" , "cover" , "language")

    def create(self, validated_data):
        return Book.objects.create(**validated_data)




