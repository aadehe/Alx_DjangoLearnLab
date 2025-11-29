from django.shortcuts import render
from rest_framework import generics
from models import Book
from serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


# Create your views here.

# ---------------------------------------------------------
# BookListView
# ---------------------------------------------------------
# Provides: GET /books/
# - Lists all books.
# - Read-only for anyone (unauthenticated users allowed).
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # Read-only access for all

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




