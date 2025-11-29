from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from models import Book
from serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


# ---------------------------------------------------------
# BookListView with Filtering, Searching, Ordering
# ---------------------------------------------------------
# Query capabilities:
# - Filtering: ?title=Foundation&publication_year=1951
# - Searching: ?search=robot
# - Ordering: ?ordering=title  OR  ?ordering=-publication_year
#
# Filtering uses DjangoFilterBackend.
# Searching uses SearchFilter.
# Ordering uses OrderingFilter.
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # Read-only access for all
    # Add advanced query features:
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    # Enable filtering by these model fields
    filterset_fields = ['title', 'publication_year', 'author']

    # Enable text search on these fields
    search_fields = ['title', 'author__name']

    # Allow ordering of results
    ordering_fields = ['title', 'publication_year']

    # Provide a default ordering
    ordering = ['title']

# ---------------------------------------------------------
# BookDetailView
# ---------------------------------------------------------
# Provides: GET /books/<pk>/
# - Retrieves a single book by ID.
# - Read-only for all.
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Read-only access for all

# ---------------------------------------------------------
# BookCreateView
# ---------------------------------------------------------
# Provides: POST /books/create/
# - Creates a new book.
# - Requires authentication.
# - Custom behavior: validate data on creation, and you can
#   add custom logic (logging, notifications, etc.)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    # Custom behavior: Example log before save
    def perform_create(self, serializer):
        # Example: print log or hook custom logic
        print(f"Creating new book: {serializer.validated_data}")
        serializer.save()

# ---------------------------------------------------------
# BookUpdateView
# ---------------------------------------------------------
# Provides: PUT/PATCH /books/<pk>/update/
# - Updates an existing book.
# - Requires authentication.
# - Custom validation handled by the serializer automatically.
class BookUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        print(f"Updating book ID={self.kwargs['pk']}")
        serializer.save()

# ---------------------------------------------------------
# BookDeleteView
# ---------------------------------------------------------
# Provides: DELETE /books/<pk>/delete/
# - Deletes a book.
# - Requires authentication.
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]




