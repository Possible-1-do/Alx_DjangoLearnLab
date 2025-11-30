"""
Serializers:
- BookSerializer: Serializes Book model fields and includes custom validation
  to ensure publication_year is not set in the future.

- AuthorSerializer: Serializes the Author model and includes a nested
  BookSerializer to display all related books dynamically.

Relationship Handling:
- The nested serializer (books = BookSerializer(many=True)) automatically uses
  the related_name 'books' defined in Book.author ForeignKey.
"""

from rest_framework import serializers
from .models import Author, Book
from datetime import datetime


# BookSerializer:
# Serializes all book fields.
# Includes custom validation to prevent publication dates in the future.
class BookSerializer(serializers.ModelSerializer):

    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']


# AuthorSerializer:
# Serializes author name and includes nested book data.
# Uses BookSerializer to serialize the related books through 'books' related_name.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)   # nested serializer

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
