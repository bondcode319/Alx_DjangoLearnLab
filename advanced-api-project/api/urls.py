from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    # List and Create endpoint
    path('books/', 
         BookListView.as_view(), 
         name='book-list'),
    path('books/create/', 
         BookCreateView.as_view(), 
         name='book-create'),
    
    # Retrieve, Update, and Delete endpoint
    path('books/<int:pk>/', 
         BookDetailView.as_view(), 
         name='book-detail'),
    path('books/<int:pk>/update/', 
         BookUpdateView.as_view(), 
         name='book-update'),
    path('books/<int:pk>/delete/', 
         BookDeleteView.as_view(), 
         name='book-delete'),
]