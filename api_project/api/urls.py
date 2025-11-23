from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Create the router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

# URL patterns
urlpatterns = [
    # Existing ListAPIView route
    path('books/', BookList.as_view(), name='book-list'),

    # Include the router URLs for BookViewSet (all CRUD)
    path('', include(router.urls)),
]
