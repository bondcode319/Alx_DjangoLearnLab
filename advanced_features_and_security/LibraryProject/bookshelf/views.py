
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from .models import Book

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
        # Add your book creation logic here
        pass
    return render(request, 'bookshelf/create_book.html')

@permission_required('bookshelf.can_edit_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        # Add your book editing logic here
        pass
    return render(request, 'bookshelf/edit_book.html', {'book': book})

@permission_required('bookshelf.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/delete_book.html', {'book': book})