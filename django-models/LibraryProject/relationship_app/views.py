# relationship_app/views.py

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Book, Author, Librarian
from .models import Library


def list_books(request):
    """
    Function-based view that lists all books stored in the database.
    Renders a simple text list of book titles and their authors.
    """
    books = Book.objects.select_related('author').all()
    context = {
        'books': books
    }
    return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
    """
    Class-based view that displays details for a specific library,
    listing all books available in that library.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get all books in this library
        context['books'] = self.object.books.select_related('author').all()
        # Get the librarian for this library (if exists)
        try:
            context['librarian'] = self.object.librarian
        except Librarian.DoesNotExist:
            context['librarian'] = None
        return context