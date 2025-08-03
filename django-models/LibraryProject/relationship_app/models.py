from django.db import models

# Create your models here.
# class Author(models.Model):
#     name = models.CharField(max_length=200),

# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    
    
# class Library(models.Model):
#     name = models.CharField(max_length=200)
#     books = models.ManyToManyField(Book, related_name='libraries')

# class Librarian(models.Model):
#     name = models.CharField(max_length=200)
#     library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')
    

    # def __str__(self):
    #     return self.name


# from django.db import models
# from django.contrib.auth.models import User

# class Author(models.Model):
#     name = models.CharField(max_length=100)
    
#     def __str__(self):
#         return self.name

# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     publication_year = models.IntegerField()
#     isbn = models.CharField(max_length=13, unique=True)
#     pages = models.IntegerField()
#     cover = models.URLField(blank=True)
#     language = models.CharField(max_length=50, default='English')
    
#     class Meta:
#         permissions = [
#             ("can_add_book", "Can add book"),
#             ("can_change_book", "Can change book"),
#             ("can_delete_book", "Can delete book"),
#         ]
    
#     def __str__(self):
#         return f"{self.title} by {self.author.name}"

# class Library(models.Model):
#     name = models.CharField(max_length=100)
#     books = models.ManyToManyField(Book)
    
#     def __str__(self):
#         return self.name

# class Librarian(models.Model):
#     library = models.OneToOneField(Library, on_delete=models.CASCADE)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return f"Librarian: {self.user.username} at {self.library.name}"

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')
    bio = models.TextField(max_length=500, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(max_length=200, blank=True)
    profile_picture = models.URLField(blank=True)
    
    class Meta:
        permissions = [
            ("can_view_member_details", "Can view member details"),
            ("can_edit_member_details", "Can edit member details"),
        ]
    
    def __str__(self):
        return f"{self.user.username} - {self.role}"
        
    def is_admin(self):
        return self.role == 'Admin'
        
    def is_librarian(self):
        return self.role == 'Librarian'
        
    def is_member(self):
        return self.role == 'Member'

class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField()
    isbn = models.CharField(max_length=13, unique=True)
    pages = models.IntegerField()
    cover = models.URLField(blank=True)
    language = models.CharField(max_length=50, default='English')
    
    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]
    
    def __str__(self):
        return f"{self.title} by {self.author.name}"

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)
    
    def __str__(self):
        return self.name

class Librarian(models.Model):
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Librarian: {self.user.username} at {self.library.name}"