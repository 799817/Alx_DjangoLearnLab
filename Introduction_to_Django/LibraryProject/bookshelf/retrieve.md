from bookshelf.models import Book

# Retrieve the book we created
book = Book.objects.get(title="1984")  # or title="Nineteen Eighty-Four" if updated
book
