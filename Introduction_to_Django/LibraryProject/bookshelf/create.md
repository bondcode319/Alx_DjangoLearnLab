
from bookshelf.models import Book
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

# Display the created book
print(book)
print(f"Book ID: {book.id}")
Expected Output


"""1984 by George Orwell (1949)
Book ID: 1"""