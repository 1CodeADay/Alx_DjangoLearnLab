import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return author.books.all()

# List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# Retrieve the librarian for a library
def get_librarian(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian

# Example usage
if __name__ == "__main__":
    author_books = books_by_author("J.K. Rowling")
    print("Books by J.K. Rowling:", [book.title for book in author_books])

    library_books = books_in_library("Central Library")
    print("Books in Central Library:", [book.title for book in library_books])

    librarian = get_librarian("Central Library")
    print("Librarian of Central Library:", librarian.name)
