from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Author, Book
from .serializers import BookSerializer

class BookAPITests(APITestCase):
    """Test suite for Book API views"""

    def setUp(self):
        """Initialize test data"""
        # Create test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
        # Create test author
        self.author = Author.objects.create(name='Test Author')
        
        # Create test books
        self.book1 = Book.objects.create(
            title='Test Book 1',
            publication_year=2020,
            author=self.author
        )
        self.book2 = Book.objects.create(
            title='Another Book',
            publication_year=2021,
            author=self.author
        )
        
        # URLs
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', args=[self.book1.pk])

    def test_get_book_list(self):
        """Test retrieving list of books"""
        response = self.client.get(self.list_url)
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data(), serializer.data)  # Use response.json() instead of data

    def test_create_book_authenticated(self):
        """Test creating a book when authenticated"""
        self.client.login(username='testuser', password='testpass123')
        data = {
            'title': 'New Book',
            'publication_year': 2023,
            'author': self.author.pk
        }
        
        response = self.client.post(self.list_url, data, format='json')  # Added format='json'
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        """Test creating a book when unauthenticated"""
        data = {
            'title': 'New Book',
            'publication_year': 2023,
            'author': self.author.pk
        }
        
        response = self.client.post(self.list_url, data, format='json')  # Added format='json'
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_book_authenticated(self):
        """Test updating a book when authenticated"""
        self.client.login(username='testuser', password='testpass123')
        data = {
            'title': 'Updated Title',
            'publication_year': 2022,
            'author': self.author.pk
        }
        
        response = self.client.put(self.detail_url, data, format='json')  # Added format='json'
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()  # Refresh from database
        self.assertEqual(self.book1.title, 'Updated Title')

    def test_delete_book_authenticated(self):
        """Test deleting a book when authenticated"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filtering_books(self):
        """Test filtering books by title"""
        response = self.client.get(f'{self.list_url}?title=Test')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_json = response.json()
        self.assertEqual(len(response_json), 1)
        self.assertEqual(response_json[0]['title'], 'Test Book 1')

    def test_searching_books(self):
        """Test searching books"""
        response = self.client.get(f'{self.list_url}?search=Another')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_json = response.json()
        self.assertEqual(len(response_json), 1)
        self.assertEqual(response_json[0]['title'], 'Another Book')

    def test_ordering_books(self):
        """Test ordering books by publication year"""
        response = self.client.get(f'{self.list_url}?ordering=-publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_json = response.json()
        self.assertEqual(response_json[0]['publication_year'], 2021)