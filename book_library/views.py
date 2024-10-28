from rest_framework import viewsets

from book_library.models import Book
from book_library.serializers import BookSerializer, BookCreateSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    model = Book
    serializer_class = BookSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return BookSerializer
        elif self.action == "create":
            return BookCreateSerializer
        return BookSerializer


    def get_queryset(self):
        queryset = Book.objects.all()
        author = self.request.query_params.get("author")
        published_date = self.request.query_params.get("published_date")
        language = self.request.query_params.get("language")


        if author:
            queryset = queryset.filter(
                author__icontains=author
            )
        if published_date:
            queryset = queryset.filter(
                published_date__icontains=published_date
            )
        if language:
            queryset = queryset.filter(
                language__icontains=language
            )
        return queryset.distinct()

