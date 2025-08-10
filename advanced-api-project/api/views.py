from django.shortcuts import render, get_object_or_404
from rest_framework import generics, permissions, filters
from django_filters import rest_framework as django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
from .filters import BookFilter
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListCreateAPIView):
    """
    API endpoint for listing and creating books.
    
    Filtering:
    - title: ?title=harry
    - publication_year: ?publication_year=2023
    - publication_year range: ?publication_year_min=2000&publication_year_max=2023
    - author name: ?author_name=rowling
    
    Searching:
    - Search across title and author name: ?search=potter
    
    Ordering:
    - Order by fields: ?ordering=publication_year
    - Reverse order: ?ordering=-publication_year
    - Multiple fields: ?ordering=publication_year,title
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = BookFilter
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year', 'author__name']
    ordering = ['publication_year']  # default ordering
    
    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        """Custom create method to handle book creation"""
        serializer.save()

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for retrieving, updating, and deleting books.
    
    GET: Retrieve book details (available to all users)
    PUT/PATCH: Update book details (requires authentication)
    DELETE: Remove book (requires authentication)
    
    Permissions:
    - GET: Allow any
    - PUT/PATCH/DELETE: Require authentication
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def update(self, request, *args, **kwargs):
        """Custom update method with additional validation"""
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """Custom delete method with confirmation response"""
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            "message": f"Book '{instance.title}' has been deleted successfully"
        }, status=status.HTTP_204_NO_CONTENT)

class BookCreateView(generics.CreateAPIView):
    """API endpoint for creating books."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class BookUpdateView(generics.UpdateAPIView):
    """API endpoint for updating books."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()

class BookDeleteView(generics.DestroyAPIView):
    """API endpoint for deleting books."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        instance.delete()
