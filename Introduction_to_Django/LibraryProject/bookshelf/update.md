from bookshelf.models import Book

# Retrieve the book to update
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Display the updated book
print(f"Updated book: {book}")
print(f"New title: {book.title}")
Expected Output

"""Updated book: Nineteen Eighty-Four by George Orwell (1949)
New title: Nineteen Eighty-Four"""