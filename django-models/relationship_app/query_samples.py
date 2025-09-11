import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
try:
    author = Author.objects.get(name="George Orwell")
    books_by_author = Book.objects.filter(author=author)
    print("Books by George Orwell:", list(books_by_author))
except Author.DoesNotExist:
    print("Author 'George Orwell' not found. Please add them first.")

# List all books in a library
try:
    library = Library.objects.get(name="Central Library")
    all_books_in_library = library.books.all()
    print("Books in Central Library:", list(all_books_in_library))
except Library.DoesNotExist:
    print("Library 'Central Library' not found. Please add it first.")

# Retrieve the librarian for a library
try:
    librarian = Librarian.objects.get(library__name="Central Library")
    print("Librarian for Central Library:", librarian.name)
except Librarian.DoesNotExist:
    print("No librarian found for Central Library. Please add one first.")
