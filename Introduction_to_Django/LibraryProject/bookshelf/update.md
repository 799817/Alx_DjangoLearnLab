```python
from bookshelf.models import Book
book1 = Book.objects.get(title="1984")
book1.title = "Nineteen Eighty-Four"
book1.save()
book1
# Output: <Book: Nineteen Eighty-Four by George Orwell (1949)>
