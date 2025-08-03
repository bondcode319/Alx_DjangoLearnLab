from api.views import BookList
from django.urls import path, include

app_name = 'api'  # Add namespace for the API


urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]
