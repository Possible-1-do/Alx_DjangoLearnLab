from rest_framework import viewsets, permissions
from rest_framework import generics
from .serializers import BookSerializer
from bookshelf.models import Book

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
# New ViewSet for all CRUD operations
class BookViewSet(viewsets.ModelViewSet):
    """
    BookViewSet provides CRUD operations for the Book model.
    Permissions: Only authenticated users can access.
    Authentication: TokenAuthentication is required for all requests.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer  
    permission_classes = [permissions.IsAuthenticated]  # Only logged-in users can access  


# Create your views here.
