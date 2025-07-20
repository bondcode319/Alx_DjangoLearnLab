
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

urlpatterns = [
    # Book listing and detail views (no special permissions required)
    path('books/', views.list_books, name='list_books'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    
    # Secured book management views with permission requirements
    path('book/add/', views.add_book, name='add_book'),  # Requires can_add_book permission
    path('book/<int:pk>/edit/', views.edit_book, name='edit_book'),  # Requires can_change_book permission
    path('book/<int:pk>/delete/', views.delete_book, name='delete_book'),  # Requires can_delete_book permission
    
    # Alternative pattern for the manage_book view (optional)
    path('book/manage/<str:action>/', views.manage_book, name='manage_book'),
    path('book/manage/<str:action>/<int:pk>/', views.manage_book, name='manage_book_with_id'),
    
    # Library and Author views
    path('library/<int:pk>/', views.library_detail, name='library_detail'),
    path('author/<int:pk>/', views.author_detail, name='author_detail'),
]