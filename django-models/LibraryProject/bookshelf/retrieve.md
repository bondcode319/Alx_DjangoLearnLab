from bookshelf.models import Book

# Retrieve the book by title
book = Book.objects.get(title="1984")

# Display all attributes
print(f"ID: {book.id}")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")
print(f"Full representation: {book}")


"""ID: 1
Title: 1984
Author: George Orwell
Publication Year: 1949
"""