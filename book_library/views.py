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

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

