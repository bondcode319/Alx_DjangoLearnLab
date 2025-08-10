from django.db import models

class Author(models.Model):
    """
    Author model representing a book author.
    
    Fields:
        name: The full name of the author
    
    The Author model has a one-to-many relationship with the Book model,
    meaning one author can have multiple books. This relationship is 
    established through the 'books' reverse relation.
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Book model representing a book in the system.
    
    Fields:
        title: The title of the book
        publication_year: The year the book was published
        author: Foreign key relationship to the Author model
    
    The Book model is related to Author through a many-to-one relationship,
    where each book must have exactly one author.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE, 
        related_name='books'
    )

    def __str__(self):
        return self.title
