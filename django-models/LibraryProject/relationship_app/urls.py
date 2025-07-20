
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

from django.urls import path
from . import views

# Define the app namespace
app_name = 'relationship_app'

urlpatterns = [
    # Function-based view: List all books
    path('books/', views.list_books, name='list_books'),
    
    # Class-based view: Library detail view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    
    # Authentication URLs
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('register/', views.register_view, name='register'),
]