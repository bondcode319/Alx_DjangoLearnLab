from django.urls import path
from .views import (
    BookListView, 
    BookDetailView, 
    BookUpdateView,
    BookDeleteView
)

urlpatterns = [
    # List and Create endpoint
    path('books/', 
         BookListView.as_view(), 
         name='book-list'),
    # path('books/create/', 
    #      BookCreateView.as_view(), 
    #      name='book-create'),
    # Retrieve, Update, and Delete endpoints
    path('books/<int:pk>/', 
         BookDetailView.as_view(), 
         name='book-detail'),
    path('books/update/',
         BookUpdateView.as_view(),
         name='book-update'),
    path('books/delete/',
         BookDeleteView.as_view(),
         name='book-delete'),
]