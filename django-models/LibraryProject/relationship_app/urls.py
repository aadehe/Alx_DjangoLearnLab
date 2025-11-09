from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Function-Based View
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-Based View

# Authentication routes
    # Authentication URLs
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
]
