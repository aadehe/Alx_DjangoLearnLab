from django.urls import path

from api_project.api.views import BookList

urlpatterns = [
    path("books/", BookList.as_view(), name="book-list"), # Maps to the BookList view

]