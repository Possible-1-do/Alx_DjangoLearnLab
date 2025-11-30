from django.db import models

# Author Model:
# Stores author information.
# One author can have many related books.
class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# Book Model:
# Stores books written by authors.
# Each book belongs to one author via ForeignKey (one-to-many relationship).
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

