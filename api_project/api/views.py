
from rest_framework import generics, permissions, viewsets, authentication
from rest_framework.permissions import AllowAny

from .models import Book
from .serializers import BookSerializer


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [AllowAny]



