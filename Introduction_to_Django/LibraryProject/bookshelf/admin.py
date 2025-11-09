from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")   # columns displayed in admin table
    search_fields = ("title", "author")                      # adds search by title and author
    list_filter = ("publication_year",)                      # add filter by year in the sidebar
