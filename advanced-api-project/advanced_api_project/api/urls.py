from django.urls import path
from .views import BookListView, BookDetailView

urlpatterns = [
    # List and Create endpoint
    path('books/', 
         BookListView.as_view(), 
         name='book-list'),
    
    # Retrieve, Update, and Delete endpoint
    path('books/<int:pk>/', 
         BookDetailView.as_view(), 
         name='book-detail'),
]