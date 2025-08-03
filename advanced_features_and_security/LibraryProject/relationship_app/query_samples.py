from django.db import connection

def get_all_librarians():
    with connection.cursor() as cursor:
        cursor.execute("SELECT librarian FROM relationship_app_librarian;")
        rows = cursor.fetchall()
    return rows
# This query retrieves all librarians from the relationship_app_librarian table.

import os
import django
from django.core.exceptions import ObjectDoesNotExist

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

# Import models after Django setup
from relationship_app.models import Author, Book, Library, Librarian


def query_all_books_by_author(author_name):
    """
    Query all books by a specific author.
    """
    try:
        # Get the author object
        author = Author.objects.get(name=author_name)
        
        # Query all books by this author using the ForeignKey relationship
        books = Book.objects.filter(author=author)
        
        # Alternative approach using reverse relationship
        # books = author.books.all()
        
        print(f"Books by {author_name}:")
        if books:
            for book in books:
                print(f"  - {book.title}")
        else:
            print(f"  No books found by {author_name}")
        
        return books
        
    except ObjectDoesNotExist:
        print(f"Author '{author_name}' not found.")
        return None


def list_all_books_in_library(library_name):
    """
    List all books in a library.
    """
    try:
        # Get the library object
        library = Library.objects.get(name=library_name)
        
        # Query all books in this library using the ManyToManyField relationship
        books = library.books.all()
        
        # Alternative approach using reverse relationship
        # books = Book.objects.filter(libraries=library)
        
        print(f"Books in {library_name} Library:")
        if books:
            for book in books:
                print(f"  - {book.title} by {book.author.name}")
        else:
            print(f"  No books found in {library_name} Library")
        
        return books
        
    except ObjectDoesNotExist:
        print(f"Library '{library_name}' not found.")
        return None


def retrieve_librarian_for_library(library_name):
    """
    Retrieve the librarian for a library.
    """
    try:
        # Get the library object
        library = Library.objects.get(name=library_name)
        
        # Get the librarian using the correct relationship
        librarian = Librarian.objects.get(library=library)
        if librarian:
            print(f"Librarian for {library_name} Library: {librarian.name}")
            return librarian
        else:
            print(f"No librarian found for {library_name} Library.")
            return None
    except ObjectDoesNotExist:
        print(f"Library '{library_name}' not found.")
        return None