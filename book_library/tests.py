from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from book_library.models import Book
from book_library.serializers import BookSerializer


class BookViewSetTests(APITestCase):

    def setUp(self):
        self.book1_0 = Book.objects.create(
            title="Book 1.0",
            author="Author One",
            published_date="2024-01-01",
            language="English",
            isbn=1111111111,
            pages=5,
            cover="https://st5.depositphotos.com/2274151/66866/v/450/depositphotos_668664232-stock-illustration-panda-hand-drawn-comic-illustration.jpg",
        )
        self.book1_1 = Book.objects.create(
            title="Book 1.1",
            author="Author One",
            published_date="2024-01-02",
            language="English",
            isbn=1111111112,
            pages=5,
            cover="https://st5.depositphotos.com/2274151/66866/v/450/depositphotos_668664232-stock-illustration-panda-hand-drawn-comic-illustration.jpg",
        )

        self.book2_0 = Book.objects.create(
            title="Book 2.0",
            author="Author Two",
            published_date="2024-02-03",
            language="Spanish",
            isbn=2222222222220,
            pages=5,
            cover="https://st5.depositphotos.com/2274151/66866/v/450/depositphotos_668664232-stock-illustration-panda-hand-drawn-comic-illustration.jpg",
        )

        self.book2_1 = Book.objects.create(
            title="Book 2.1",
            author="Author Two",
            published_date="2024-02-04",
            language="Spanish",
            isbn=2222222222221,
            pages=5,
            cover="https://st5.depositphotos.com/2274151/66866/v/450/depositphotos_668664232-stock-illustration-panda-hand-drawn-comic-illustration.jpg",
        )

        self.book3_0 = Book.objects.create(
            title="Book 3.0",
            author="Author Three",
            published_date="2024-02-05",
            language="German",
            isbn=33333333330,
            pages=5,
            cover="https://st5.depositphotos.com/2274151/66866/v/450/depositphotos_668664232-stock-illustration-panda-hand-drawn-comic-illustration.jpg",
        )

        self.book3_1 = Book.objects.create(
            title="Book 3.0",
            author="Author Three",
            published_date="2024-03-06",
            language="German",
            isbn=33333333331,
            pages=5,
            cover="https://st5.depositphotos.com/2274151/66866/v/450/depositphotos_668664232-stock-illustration-panda-hand-drawn-comic-illustration.jpg",
        )

        self.book4_0 = Book.objects.create(
            title="Book 4.0",
            author="Author Four",
            published_date="2024-03-01",
            language="French",
            isbn=4444444440,
            pages=7,
            cover="https://example.com/image7.jpg",
        )

        self.book4_1 = Book.objects.create(
            title="Book 4.1",
            author="Author Four",
            published_date="2024-03-02",
            language="French",
            isbn=4444444441,
            pages=8,
            cover="https://example.com/image8.jpg",
        )

        self.book5_0 = Book.objects.create(
            title="Book 5.0",
            author="Author Five",
            published_date="2024-03-03",
            language="Italian",
            isbn=5555555550,
            pages=6,
            cover="https://example.com/image9.jpg",
        )

        self.book5_1 = Book.objects.create(
            title="Book 5.1",
            author="Author Five",
            published_date="2024-03-04",
            language="Italian",
            isbn=5555555551,
            pages=9,
            cover="https://example.com/image10.jpg",
        )

        self.book6_0 = Book.objects.create(
            title="Book 6.0",
            author="Author Six",
            published_date="2024-03-05",
            language="Portuguese",
            isbn=6666666660,
            pages=4,
            cover="https://example.com/image11.jpg",
        )

        self.book6_1 = Book.objects.create(
            title="Book 6.1",
            author="Author Six",
            published_date="2024-03-06",
            language="Portuguese",
            isbn=6666666661,
            pages=5,
            cover="https://example.com/image12.jpg",
        )

    """
    CRUD Testing
    """

    def test_list_books(self):
        """Test the API endpoint for listing books with pagination."""

        url = reverse("book_library:book-list")
        response_page_1 = self.client.get(url + "?page=1")
        response_page_2 = self.client.get(url + "?limit=10&offset=10&page=next")

        self.assertEqual(response_page_1.status_code, status.HTTP_200_OK,
                         f"Expected status code 200, but got {response_page_1.status_code}.")

        self.assertEqual(response_page_2.status_code, status.HTTP_200_OK,
                         f"Expected status code 200, but got {response_page_2.status_code}.")

        self.assertEqual(len(response_page_1.data["results"]), 10,
                         f"Expected 10 books on page 1, but got {len(response_page_1.data['results'])}.")

        self.assertEqual(len(response_page_2.data["results"]), 2,
                         f"Expected 2 books on page 2, but got {len(response_page_2.data['results'])}.")

        self.assertEqual(
            len(response_page_1.data['results']) + len(response_page_2.data['results']),
            12,
            f"Expected a total of 12 books across both pages, but got {len(response_page_1.data['results']) + len(response_page_2.data['results'])}.")

    def test_create_book(self):
        """Testing the creation of a new book"""
        url = reverse("book_library:book-list")
        data = {
            "title": "Book 4.0",
            "author": "Author Four",
            "published_date": "2024-03-06",
            "language": "German",
            "isbn": 9876543210,
            "pages": 5,
            "cover": "https://st5.depositphotos.com/2274151/66866/v/450/depositphotos_668664232-stock-illustration-panda-hand-drawn-comic-illustration.jpg"
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED,
                         f"Expected 201 Created, got {response.status_code}. Response data: {response.data}")

    def test_update_book(self):
        """Test updating a book's details in the library."""
        url = reverse("book_library:book-detail", args=[self.book1_0.id])
        data = {
            "title": "Updated Book Title",
            "author": "Updated Author",
            "published_date": "2024-01-10",
            "language": "English",
            "isbn": 9999999999,
            "pages": 10,
            "cover": "https://example.com/image9.jpg"
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         "Assertion failed: Response status code is not 200 OK after updating the book.")
        self.book1_0.refresh_from_db()  # Обновляем объект из базы данных
        self.assertEqual(self.book1_0.title, "Updated Book Title",
                         "Assertion failed: Book title was not updated as expected.")

    def test_delete_book(self):
        """Test delete a book's details in the library."""
        url = reverse("book_library:book-detail", args=[self.book1_0.id])  # URL для удаления книги
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT,
                         "Assertion failed: Response status code is not 204 No Content after deleting the book.")
        self.assertFalse(Book.objects.filter(id=self.book1_0.id).exists(),
                         "Assertion failed: Book was not deleted from the database.")

    """
    Filtering Testing
    """

    def test_filter_books_by_author(self):
        """ Test filtering books by author."""

        url = reverse("book_library:book-list") + "?author=Author One"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 2,
                         "Assertion failed: the number of books filtered by author in the response does not match the expected count.")

    def test_filter_books_by_published_date(self):
        """Test filtering books by published date."""
        url = reverse("book_library:book-list") + "?published_date=2024-01-01"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)

    def test_filter_books_by_language(self):
        """Test filtering books by language."""
        url = reverse("book_library:book-list") + "?language=English"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 2)

    """
    Any test
    """

    def test_pagination(self):
        """Test the pagination of the book list."""

        url = reverse("book_library:book-list")
        response_page_1 = self.client.get(url)
        response_page_2 = self.client.get(url + "?limit=10&offset=10&page=next")

        self.assertEqual(response_page_1.status_code, status.HTTP_200_OK,
                         f"Expected response status code 200 OK, but got {response_page_1.status_code}.")
        self.assertEqual(response_page_2.status_code, status.HTTP_200_OK,
                         f"Expected response status code 200 OK, but got {response_page_1.status_code}.")

        self.assertEqual(len(response_page_1.data["results"]), 10,
                         f"Expected 10 books on the first page, but got {len(response_page_1.data['results'])}.")

        self.assertEqual(len(response_page_2.data["results"]), 2,
                         f"Expected 2 books on page 2, but got {len(response_page_2.data['results'])}.")

    def test_serialization(self):
        """Testing book serialization"""
        url = reverse("book_library:book-detail", args=[self.book1_0.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         "Assertion failed: Response status code is not 200 OK.")

        serializer = BookSerializer(self.book1_0)
        self.assertEqual(response.data, serializer.data,
                         "Assertion failed: Response data does not match the expected serialized data.")
