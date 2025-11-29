import datetime

from rest_framework import serializers
from .models import Book, Author


# ------------------------------------------------
# BookSerializer
# ------------------------------------------------
# Serializes all fields of the Book model.
# Includes custom validation to ensure the
# publication year is not in the future.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__' # serialize all book fields

        # Custom validation: publication_year must not be in the future
        def validate_publication_year(self, value):
            current_year = datetime.datetime.now().year
            if value > current_year:
                raise serializers.ValidationError(
                    'Publication year cannot be greater than current year'
                )
            return value


# ------------------------------------------------
# AuthorSerializer
# ------------------------------------------------
# Serializes the Author model.
# Includes nested serialization of related books
# using the BookSerializer with many=True.
#
# The nested representation allows all books for an author
# to be included automatically.
class AuthorSerializer(serializers.ModelSerializer):
    # Nested serializer — read-only list of related books
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = (
            'id',
            'name',
            'books'
        )

