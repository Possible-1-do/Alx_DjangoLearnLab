from rest_framework import viewsets
from rest_framework import generics
from .serializers import BookSerializer
from bookshelf.models import Book

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
# New ViewSet for all CRUD operations
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer    


# Create your views here.
