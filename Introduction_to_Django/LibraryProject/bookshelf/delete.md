```python
from bookshelf.models import Book
book1 = Book.objects.get(title="Nineteen Eighty-Four")
book1.delete()
Book.objects.all()
# Output: <QuerySet []>
