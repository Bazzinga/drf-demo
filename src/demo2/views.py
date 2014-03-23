from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book

class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint for my very sophisticated book model
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
