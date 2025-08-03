from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from .models import Book
from .serializers import BookSerializer


class BookList(generics.ListAPIView):
    """
    API endpoint that provides read-only access to books.
    
    Authentication:
    - Uses Token Authentication
    - Requires valid token in Authorization header for write operations
    
    Permissions:
    - Anonymous users can view books (GET)
    - Only authenticated users can perform write operations
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing Book instances.

    Authentication:
    - Uses Token Authentication from REST framework
    - Include token in request header: Authorization: Token <your-token>
    
    Permissions:
    - List and Retrieve (GET): Available to all users (AllowAny)
    - Create, Update, Delete (POST, PUT, DELETE): Requires authentication
    
    Endpoints:
    - GET /books_all/ - List all books
    - POST /books_all/ - Create a new book (auth required)
    - GET /books_all/{id}/ - Retrieve a specific book
    - PUT /books_all/{id}/ - Update a book (auth required)
    - DELETE /books_all/{id}/ - Delete a book (auth required)
    
    Example Authorization header:
    Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        """
        Override to customize permissions based on action:
        - 'list' and 'retrieve' actions are public
        - All other actions require authentication
        """
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]


