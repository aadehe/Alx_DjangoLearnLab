from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    # One-to-many: One Author → Many Books
    authors = models.ForeignKey(
        Author,
        on_delete=models.PROTECT,
        related_name='books'
    )

    def __str__(self):
        return self.title


