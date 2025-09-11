import os
import sys
import django

# Add the project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Point to the correct settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")

django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Sample queries
def run_queries():
    # Query all books by a specific author
    try:
        author = Author.objects.get(name="George Orwell")
        books_by_author = Book.objects.filter(author=author)
        print("Books by George Orwell:", [book.title for book in books_by_author])
    except Author.DoesNotExist:
        print("Author 'George Orwell' not found. Please add them first.")

    # List all books in a library
    try:
        library = Library.objects.get(name="Central Library")
        print("Books in Central Library:", [book.title for book in library.books.all()])
    except Library.DoesNotExist:
        print("Library 'Central Library' not found. Please add it first.")

    # Retrieve the librarian for a library
    try:
        library = Library.objects.get(name="Central Library")
        librarian = Librarian.objects.get(library=library)
        print("Librarian of Central Library:", librarian.name)
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        print("No librarian found for Central Library. Please add one first.")


if __name__ == "__main__":
    run_queries()
