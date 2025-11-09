from django.urls import path
from .views import list_books, LibraryDetailView, login_view, logout_view, register_view

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Function-Based View
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-Based View

# Authentication routes
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
]
