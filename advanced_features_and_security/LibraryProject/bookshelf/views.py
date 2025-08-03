
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from .models import Book
from .forms import BookForm  # Make sure you have a BookForm defined
from django import forms
from .forms import ExampleForm

class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False)

def index(request):
    return HttpResponse('Welcome to my second project.')

@permission_required('bookshelf.can_view_details', raise_exception=True)
def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if book.is_restricted and not request.user.has_perm('bookshelf.can_view_restricted'):
        raise PermissionDenied
    return render(request, 'bookshelf/book_detail.html', {'book': book})

@permission_required('bookshelf.can_create_book', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/create_book.html', {'form': form})

@permission_required('bookshelf.can_edit_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/edit_book.html', {'form': form, 'book': book})

@permission_required('bookshelf.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/delete_book.html', {'book': book})

def search_books(request):
    form = BookSearchForm(request.GET)
    books = Book.objects.none()
    if form.is_valid():
        query = form.cleaned_data['query']
        books = Book.objects.filter(title__icontains=query)
    return render(request, 'bookshelf/search_results.html', {'form': form, 'books': books})