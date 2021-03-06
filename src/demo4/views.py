from rest_framework import viewsets
from .serializers import BookSerializer, LeanBookSerializer
from .models import Book
from .filters import BookFilter

class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint for my very sophisticated book model
    """
    # Demo #4
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filter_class = BookFilter

    def get_serializer_class(self):
        if self.get_view_name() == 'Book List':
            return LeanBookSerializer
        else:
            return BookSerializer
