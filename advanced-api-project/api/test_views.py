from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse
from api.models import Author, Book


class BookAPITestCase(APITestCase):
    """
    Test suite for Book API endpoints.
    Covers CRUD operations, permissions, filtering,
    searching, and ordering.
    """

    def setUp(self):
        # Create user for authenticated tests
        self.user = User.objects.create_user(
            username="testuser",
            password="password123"
        )

        # Create authors
        self.author1 = Author.objects.create(name="Isaac Asimov")
        self.author2 = Author.objects.create(name="Arthur C. Clarke")

        # Create books
        self.book1 = Book.objects.create(
            title="Foundation",
            publication_year=1951,
            author=self.author1
        )
        self.book2 = Book.objects.create(
            title="I, Robot",
            publication_year=1950,
            author=self.author1
        )
        self.book3 = Book.objects.create(
            title="Childhood's End",
            publication_year=1953,
            author=self.author2
        )

        self.client = APIClient()

    # ---------------------------------------------------
    # READ TESTS
    # ---------------------------------------------------

    def test_list_books(self):
        """Anyone should be able to list all books."""
        url = reverse("book-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_retrieve_single_book(self):
        """Anyone can retrieve a single book."""
        url = reverse("book-detail", args=[self.book1.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Foundation")

    # ---------------------------------------------------
    # CREATE TESTS
    # ---------------------------------------------------

    def test_unauthenticated_create_book_fails(self):
        """Unauthenticated users cannot create books."""
        url = reverse("book-create")
        data = {
            "title": "New Book",
            "publication_year": 2020,
            "author": self.author1.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_create_book_succeeds(self):
        """Authenticated request should create a book."""
        self.client.login(username="testuser", password="password123")

        url = reverse("book-create")
        data = {
            "title": "New Book",
            "publication_year": 2020,
            "author": self.author1.id
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)

    # ---------------------------------------------------
    # UPDATE TESTS
    # ---------------------------------------------------

    def test_unauthenticated_update_fails(self):
        url = reverse("book-update", args=[self.book1.id])
        data = {"title": "Updated Title"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_update_succeeds(self):
        self.client.login(username="testuser", password="password123")

        url = reverse("book-update", args=[self.book1.id])
        data = {"title": "Updated Title"}

        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    # ---------------------------------------------------
    # DELETE TESTS
    # ---------------------------------------------------

    def test_unauthenticated_delete_fails(self):
        url = reverse("book-delete", args=[self.book1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_delete_succeeds(self):
        self.client.login(username="testuser", password="password123")

        url = reverse("book-delete", args=[self.book1.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 2)

    # ---------------------------------------------------
    # FILTERING, SEARCH, ORDERING TESTS
    # ---------------------------------------------------

    def test_filter_by_title(self):
        url = reverse("book-list") + "?title=Foundation"
        response = self.client.get(url)

        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Foundation")

    def test_filter_by_author(self):
        url = reverse("book-list") + f"?author={self.author2.id}"
        response = self.client.get(url)

        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Childhood's End")

    def test_search_books(self):
        """Search across title + author name."""
        url = reverse("book-list") + "?search=robot"
        response = self.client.get(url)

        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "I, Robot")

    def test_order_books(self):
        """Test ordering by publication_year descending."""
        url = reverse("book-list") + "?ordering=-publication_year"
        response = self.client.get(url)

        years = [book["publication_year"] for book in response.data]
        self.assertEqual(years, sorted(years, reverse=True))
