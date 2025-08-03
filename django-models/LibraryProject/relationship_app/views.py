# relationship_app/views.py

# from django.shortcuts import render, get_object_or_404
# from django.views.generic import ListView, DetailView
# from .models import Book, Author, Librarian
# from .models import Library


# def list_books(request):
#     """
#     Function-based view that lists all books stored in the database.
#     Renders a simple text list of book titles and their authors.
#     """
#     books = Book.objects.select_related('author').all()
#     context = {
#         'books': books
#     }
#     return render(request, 'relationship_app/list_books.html', context)


# class LibraryDetailView(DetailView):
#     """
#     Class-based view that displays details for a specific library,
#     listing all books available in that library.
#     """
#     model = Library
#     template_name = 'relationship_app/library_detail.html'
#     context_object_name = 'library'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # Get all books in this library
#         context['books'] = self.object.books.select_related('author').all()
#         # Get the librarian for this library (if exists)
#         try:
#             context['librarian'] = self.object.librarian
#         except Librarian.DoesNotExist:
#             context['librarian'] = None
#         return context
    
    # relationship_app/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Book, Author, Librarian
from .models import Library


# @login_required
# def list_books(request):
#     """
#     Function-based view that lists all books stored in the database.
#     Renders a simple text list of book titles and their authors.
#     """
#     books = Book.objects.select_related('author').all()
#     context = {
#         'books': books
#     }
#     return render(request, 'relationship_app/list_books.html', context)


# @method_decorator(login_required, name='dispatch')
# class LibraryDetailView(DetailView):
#     """
#     Class-based view that displays details for a specific library,
#     listing all books available in that library.
#     """
#     model = Library
#     template_name = 'relationship_app/library_detail.html'
#     context_object_name = 'library'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # Get all books in this library
#         context['books'] = self.object.books.select_related('author').all()
#         # Get the librarian for this library (if exists)
#         try:
#             context['librarian'] = self.object.librarian
#         except Librarian.DoesNotExist:
#             context['librarian'] = None
#         return context


# # Authentication Views
# def register_view(request):
#     """
#     Handle user registration
#     """
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('relationship_app:list_books')
#     else:
#         form = UserCreationForm()
    
#     return render(request, 'relationship_app/register.html', {'form': form})


# class CustomLoginView(LoginView):
#     """
#     Custom login view using Django's built-in LoginView
#     """
#     template_name = 'relationship_app/login.html'
#     redirect_authenticated_user = True
    
#     def get_success_url(self):
#         return '/books/'  # Redirect to books list after login


# class CustomLogoutView(LogoutView):
#     """
#     Custom logout view using Django's built-in LogoutView
#     """
#     template_name = 'relationship_app/logout.html'
    
    
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from .forms import BookForm  # Assuming you have a BookForm

# List view - no special permission required
# def list_books(request):
#     """Display all books"""
#     books = Book.objects.all()
#     return render(request, 'relationship_app/list_books.html', {'books': books})

# # Detail view - no special permission required
# def book_detail(request, pk):
#     """Display book details"""
#     book = get_object_or_404(Book, pk=pk)
#     return render(request, 'relationship_app/book_detail.html', {'book': book})

# # Create view with permission check
# @login_required
# @permission_required('relationship_app.can_add_book', raise_exception=True)
# def add_book(request):
#     """Add a new book - requires can_add_book permission"""
#     if request.method == 'POST':
#         form = BookForm(request.POST)
#         if form.is_valid():
#             book = form.save()
#             messages.success(request, f'Book "{book.title}" has been added successfully!')
#             return redirect('book_detail', pk=book.pk)
#     else:
#         form = BookForm()
    
#     return render(request, 'relationship_app/add_book.html', {'form': form})

# # Update view with permission check
# @login_required
# @permission_required('relationship_app.can_change_book', raise_exception=True)
# def edit_book(request):
#     """Edit an existing book - requires can_change_book permission"""
#     # Get book ID from GET or POST parameters
#     book_id = request.GET.get('id') or request.POST.get('book_id')
#     if not book_id:
#         messages.error(request, 'Book ID is required to edit a book.')
#         return redirect('list_books')
    
#     book = get_object_or_404(Book, pk=book_id)
    
#     if request.method == 'POST':
#         form = BookForm(request.POST, instance=book)
#         if form.is_valid():
#             book = form.save()
#             messages.success(request, f'Book "{book.title}" has been updated successfully!')
#             return redirect('book_detail', pk=book.pk)
#     else:
#         form = BookForm(instance=book)
    
#     return render(request, 'relationship_app/edit_book.html', {
#         'form': form, 
#         'book': book
#     })

# # Delete view with permission check
# @login_required
# @permission_required('relationship_app.can_delete_book', raise_exception=True)
# def delete_book(request):
#     """Delete a book - requires can_delete_book permission"""
#     # Get book ID from GET or POST parameters
#     book_id = request.GET.get('id') or request.POST.get('book_id')
#     if not book_id:
#         messages.error(request, 'Book ID is required to delete a book.')
#         return redirect('list_books')
    
#     book = get_object_or_404(Book, pk=book_id)
    
#     if request.method == 'POST':
#         book_title = book.title
#         book.delete()
#         messages.success(request, f'Book "{book_title}" has been deleted successfully!')
#         return redirect('list_books')
    
#     return render(request, 'relationship_app/delete_book.html', {'book': book})

# # Alternative function-based view with manual permission checking
# @login_required
# def manage_book(request, action, pk=None):
#     """
#     Alternative approach: Single view to handle multiple actions with manual permission checking
#     """
#     if action == 'add':
#         if not request.user.has_perm('relationship_app.can_add_book'):
#             return HttpResponseForbidden("You don't have permission to add books.")
#         # Add book logic here
#         pass
    
#     elif action == 'edit':
#         if not request.user.has_perm('relationship_app.can_change_book'):
#             return HttpResponseForbidden("You don't have permission to edit books.")
#         book = get_object_or_404(Book, pk=pk)
#         # Edit book logic here
#         pass
    
#     elif action == 'delete':
#         if not request.user.has_perm('relationship_app.can_delete_book'):
#             return HttpResponseForbidden("You don't have permission to delete books.")
#         book = get_object_or_404(Book, pk=pk)
#         # Delete book logic here
#         pass

# # Library and Author views (for completeness)
# def library_detail(request, pk):
#     """Display library details"""
#     library = get_object_or_404(Library, pk=pk)
#     return render(request, 'relationship_app/library_detail.html', {'library': library})

# def author_detail(request, pk):
#     """Display author details"""
#     author = get_object_or_404(Author, pk=pk)
#     return render(request, 'relationship_app/author_detail.html', {'author': author})


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required, login_required, user_passes_test
from django.contrib import messages
from django.http import HttpResponseForbidden
from .models import Book, Author, Library, UserProfile
from .forms import BookForm  # Assuming you have a BookForm

# Custom decorator to check if user has Admin role
def admin_required(view_func):
    """Decorator to check if user has Admin role"""
    def check_admin(user):
        if user.is_authenticated:
            try:
                return user.userprofile.role == 'Admin'
            except UserProfile.DoesNotExist:
                return False
        return False
    
    actual_decorator = user_passes_test(check_admin)
    return actual_decorator(view_func)

# Custom decorator to check if user has Librarian role
def librarian_required(view_func):
    """Decorator to check if user has Librarian role"""
    def check_librarian(user):
        if user.is_authenticated:
            try:
                return user.userprofile.role == 'Librarian'
            except UserProfile.DoesNotExist:
                return False
        return False
    
    actual_decorator = user_passes_test(check_librarian)
    return actual_decorator(view_func)

# Admin-only view
@login_required
@admin_required
def admin_view(request):
    """Admin dashboard - only accessible by users with Admin role"""
    # Get statistics for admin dashboard
    total_books = Book.objects.count()
    total_authors = Author.objects.count()
    total_libraries = Library.objects.count()
    total_users = UserProfile.objects.count()
    
    # Get recent books
    recent_books = Book.objects.order_by('-id')[:5]
    
    # Get user role distribution
    role_stats = {}
    for role_choice in UserProfile.ROLE_CHOICES:
        role_name = role_choice[0]
        count = UserProfile.objects.filter(role=role_name).count()
        role_stats[role_name] = count
    
    context = {
        'total_books': total_books,
        'total_authors': total_authors,
        'total_libraries': total_libraries,
        'total_users': total_users,
        'recent_books': recent_books,
        'role_stats': role_stats,
    }
    
    return render(request, 'relationship_app/admin_view.html', context)

# List view - no special permission required
def list_books(request):
    """Display all books"""
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Detail view - no special permission required
def book_detail(request, pk):
    """Display book details"""
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'relationship_app/book_detail.html', {'book': book})

# Create view with permission check
@login_required
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    """Add a new book - requires can_add_book permission"""
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            messages.success(request, f'Book "{book.title}" has been added successfully!')
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm()
    
    return render(request, 'relationship_app/add_book.html', {'form': form})

# Update view with permission check
@login_required
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request):
    """Edit an existing book - requires can_change_book permission"""
    # Get book ID from GET or POST parameters
    book_id = request.GET.get('id') or request.POST.get('book_id')
    if not book_id:
        messages.error(request, 'Book ID is required to edit a book.')
        return redirect('list_books')
    
    book = get_object_or_404(Book, pk=book_id)
    
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save()
            messages.success(request, f'Book "{book.title}" has been updated successfully!')
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    
    return render(request, 'relationship_app/edit_book.html', {
        'form': form, 
        'book': book
    })

# Delete view with permission check
@login_required
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request):
    """Delete a book - requires can_delete_book permission"""
    # Get book ID from GET or POST parameters
    book_id = request.GET.get('id') or request.POST.get('book_id')
    if not book_id:
        messages.error(request, 'Book ID is required to delete a book.')
        return redirect('list_books')
    
    book = get_object_or_404(Book, pk=book_id)
    
    if request.method == 'POST':
        book_title = book.title
        book.delete()
        messages.success(request, f'Book "{book_title}" has been deleted successfully!')
        return redirect('list_books')
    
    return render(request, 'relationship_app/delete_book.html', {'book': book})

# Alternative function-based view with manual permission checking
@login_required
def manage_book(request, action, pk=None):
    """
    Alternative approach: Single view to handle multiple actions with manual permission checking
    """
    if action == 'add':
        if not request.user.has_perm('relationship_app.can_add_book'):
            return HttpResponseForbidden("You don't have permission to add books.")
        # Add book logic here
        pass
    
    elif action == 'edit':
        if not request.user.has_perm('relationship_app.can_change_book'):
            return HttpResponseForbidden("You don't have permission to edit books.")
        book = get_object_or_404(Book, pk=pk)
        # Edit book logic here
        pass
    
    elif action == 'delete':
        if not request.user.has_perm('relationship_app.can_delete_book'):
            return HttpResponseForbidden("You don't have permission to delete books.")
        book = get_object_or_404(Book, pk=pk)
        # Delete book logic here
        pass

# Library and Author views (for completeness)
def library_detail(request, pk):
    """Display library details"""
    library = get_object_or_404(Library, pk=pk)
    return render(request, 'relationship_app/library_detail.html', {'library': library})

@login_required
@librarian_required
def library_books(request, library_id):
    """Display and manage books in a specific library"""
    library = get_object_or_404(Library, pk=library_id)
    
    # Check if the librarian is assigned to this library
    try:
        librarian = Librarian.objects.get(user=request.user, library=library)
    except Librarian.DoesNotExist:
        messages.error(request, "You don't have permission to manage this library's books.")
        return redirect('list_books')
    
    books = library.books.select_related('author').all()
    available_books = Book.objects.exclude(library=library)
    
    context = {
        'library': library,
        'books': books,
        'available_books': available_books,
    }
    return render(request, 'relationship_app/library_books.html', context)

@login_required
@librarian_required
def add_book_to_library(request, library_id):
    """Add an existing book to a library"""
    library = get_object_or_404(Library, pk=library_id)
    
    # Check if the librarian is assigned to this library
    try:
        librarian = Librarian.objects.get(user=request.user, library=library)
    except Librarian.DoesNotExist:
        messages.error(request, "You don't have permission to manage this library's books.")
        return redirect('list_books')
    
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        if book_id:
            book = get_object_or_404(Book, pk=book_id)
            library.books.add(book)
            messages.success(request, f'"{book.title}" has been added to {library.name}')
        return redirect('library_books', library_id=library.id)
    
    # Get books not in this library
    available_books = Book.objects.exclude(library=library)
    return render(request, 'relationship_app/add_book_to_library.html', {
        'library': library,
        'available_books': available_books,
    })

@login_required
@librarian_required
def remove_book_from_library(request, library_id, book_id):
    """Remove a book from a library"""
    library = get_object_or_404(Library, pk=library_id)
    
    # Check if the librarian is assigned to this library
    try:
        librarian = Librarian.objects.get(user=request.user, library=library)
    except Librarian.DoesNotExist:
        messages.error(request, "You don't have permission to manage this library's books.")
        return redirect('list_books')
    
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        library.books.remove(book)
        messages.success(request, f'"{book.title}" has been removed from {library.name}')
    
    return redirect('library_books', library_id=library.id)


def author_detail(request, pk):
    """Display author details"""
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'relationship_app/author_detail.html', {'author': author})

@login_required
@librarian_required
def librarian_dashboard(request):
    """
    Librarian dashboard - only accessible by users with Librarian role
    Shows library-specific information and management options
    """
    # Get the librarian's associated library
    try:
        librarian = Librarian.objects.get(user=request.user)
        library = librarian.library
        
        # Get library statistics
        total_books = library.books.count()
        books = library.books.select_related('author').all()
        
        context = {
            'library': library,
            'total_books': total_books,
            'books': books,
            'librarian': librarian,
        }
        
        return render(request, 'relationship_app/librarian_dashboard.html', context)
    except Librarian.DoesNotExist:
        messages.error(request, 'You need to be assigned to a library first.')
        return redirect('profile')

# User registration view
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import ExtendedUserCreationForm, UserProfileForm

def register_view(request):
    """
    Handle user registration with profile creation
    """
    if request.method == 'POST':
        user_form = ExtendedUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            
            # Create UserProfile
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            
            # Log the user in
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('list_books')
    else:
        user_form = ExtendedUserCreationForm()
        profile_form = UserProfileForm()
    
    return render(request, 'relationship_app/register.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@login_required
def profile_view(request):
    """
    View and edit user profile
    """
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user=request.user)
    
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        profile_form = UserProfileForm(instance=profile)
    
    return render(request, 'relationship_app/profile.html', {
        'profile_form': profile_form,
        'profile': profile
    })