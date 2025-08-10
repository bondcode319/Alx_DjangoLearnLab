from django_filters import rest_framework as filters
from .models import Book

class BookFilter(filters.FilterSet):
    """
    Filter set for Book model.
    
    Provides filtering capabilities for:
    - title: Case-insensitive partial matches
    - publication_year: Exact, greater than, and less than matches
    - author: Filter by author name
    """
    title = filters.CharFilter(lookup_expr='icontains')
    publication_year_min = filters.NumberFilter(field_name='publication_year', lookup_expr='gte')
    publication_year_max = filters.NumberFilter(field_name='publication_year', lookup_expr='lte')
    author_name = filters.CharFilter(field_name='author__name', lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']