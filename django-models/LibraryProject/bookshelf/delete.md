### Delete the created Book instance
from bookshelf.models import Book

```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# (1, {'bookshelf.Book': 1})
