from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    
    Serializes and deserializes Book instances to and from JSON.
    
    Fields:
        id: The book's unique identifier
        title: The book's title
        publication_year: Year of publication (with future date validation)
        author: The ID of the author
    
    Validation:
        - Ensures publication_year is not in the future
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """
        Custom validation to ensure publication year is not in the future.
        
        Args:
            value: The year to validate
            
        Returns:
            The validated year if valid
            
        Raises:
            ValidationError: If the year is in the future
        """
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                f"Publication year cannot be in the future. Current year is {current_year}"
            )
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    
    Provides a nested representation of an author and their books.
    
    Fields:
        id: The author's unique identifier
        name: The author's name
        books: Nested serializer containing all books by this author
    
    The 'books' field uses a nested BookSerializer with many=True to serialize
    all books associated with the author. The read_only=True flag ensures that
    books cannot be created directly through the author endpoint.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']