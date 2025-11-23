from rest_framework import serializers
from bookshelf.models import Book  # Import your Book model

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Include all fields of the Book model
