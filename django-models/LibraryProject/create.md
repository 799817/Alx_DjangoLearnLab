# Create Operation

```python
from bookshelf.models import Book

# Create a Book instance
book1 = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book1
# Expected output:
# <Book: 1984 by George Orwell (1949)>
