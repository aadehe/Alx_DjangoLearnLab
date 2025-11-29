from django.db import models

# Create your models here.
# -----------------------------
# Author Model
# -----------------------------
# Stores a single author's name.
# One author can have multiple related books.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# -----------------------------
# Book Model
# -----------------------------
# Represents one book written by an author.
# The `author` ForeignKey establishes a one-to-many
# relationship from Author → Book.
class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    # One-to-many: One Author → Many Books
    author = models.ForeignKey(
        Author,
        on_delete=models.PROTECT,
        related_name='books'
    )

    def __str__(self):
        return self.title


