
# relationship_app/urls.py

# from django.urls import path
# from . import views

# # Define the app namespace
# app_name = 'relationship_app'

# urlpatterns = [
#     # Function-based view: List all books
#     path('books/', views.list_books, name='list_books'),
    
#     # Class-based view: Library detail view
#     path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
# ]

# relationship_app/urls.py

# from django.urls import path
# from . import views

# # Define the app namespace
# app_name = 'relationship_app'

# urlpatterns = [
#     # Function-based view: List all books
#     path('books/', views.list_books, name='list_books'),
    
#     # Class-based view: Library detail view
#     path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    
#     # Authentication URLs
#     path('login/', views.CustomLoginView.as_view(), name='login'),
#     path('logout/', views.CustomLogoutView.as_view(), name='logout'),
#     path('register/', views.register_view, name='register'),
# ]


from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books

urlpatterns = [
    # Book listing and detail views (no special permissions required)
    path('books/', list_books, name='list_books'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    
    # Book management - requires appropriate permissions
    path('books/add/', views.add_book, name='add_book'),  # Requires can_add_book permission
    path('books/<int:pk>/edit/', views.edit_book, name='edit_book'),  # Requires can_change_book permission
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),  # Requires can_delete_book permission
    
    # Library-specific book management
    path('library/<int:library_id>/books/add/', views.add_book_to_library, name='add_book_to_library'),
    path('library/<int:library_id>/books/remove/<int:book_id>/', views.remove_book_from_library, name='remove_book_from_library'),
    path('library/<int:library_id>/books/', views.library_books, name='library_books'),
    
    # Alternative pattern for the manage_book view (optional)
    # Removed due to path converter incompatibility and view signature issues
    
    # Library and Author views
    path('library/<int:pk>/', views.library_detail, name='library_detail'),
    path('author/<int:pk>/', views.author_detail, name='author_detail'),

    # Authentication URLs
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    
    # Admin URLs
    path('admin-dashboard/', views.admin_view, name='admin_dashboard'),
    
    # Librarian URLs
    path('librarian-dashboard/', views.librarian_dashboard, name='librarian_dashboard'),
]