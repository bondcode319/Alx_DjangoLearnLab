from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'published_date', 'is_restricted')
    search_fields = ('title', 'author', 'isbn')

admin.site.register(Book, BookAdmin)