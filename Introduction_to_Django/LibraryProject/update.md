# Update Operation

```python
from bookshelf.models import Book

# Retrieve the book
book1 = Book.objects.get(title="1984")

# Update the title
book1.title = "Nineteen Eighty-Four"
book1.save()

# Verify the update
book1
# Expected output:
# <Book: Nineteen Eighty-Four by George Orwell (1949)>
