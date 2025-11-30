from django.contrib import admin
from .models import Author, Book

# Register Author model
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

# Register Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publication_year', 'author')


# Register your models here.
