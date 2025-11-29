import datetime

from rest_framework import serializers
from .models import Book, Author

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


class AuthorSerializer(serializers.ModelSerializer):
    # Nested serializer — read-only list of related books
    books = BookSerializer(many=True)
    class Meta:
        model = Author
        fields = (
            'id',
            'name',
            'books'
        )

