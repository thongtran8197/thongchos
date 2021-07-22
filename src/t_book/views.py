from rest_framework import viewsets

from .models import Book
from .serializer.book import BookSerializer


class UserViewSet(viewsets.ModelViewSet):
    view_set = "t_book"
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
