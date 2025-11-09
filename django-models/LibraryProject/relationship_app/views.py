from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import DetailView
from .models import Book, Library

# Create your views here.

# Function-Based View: List all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View: Display details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
