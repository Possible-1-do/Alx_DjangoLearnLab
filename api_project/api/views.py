from rest_framework import generics
from .serializers import BookSerializer
from bookshelf.models import Book

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# Create your views here.
