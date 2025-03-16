# bookshelf/forms.py

from django import forms
from .models import Book

# Define the form for the Book model
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_year']  # Specify the fields to include in the form

# Example of a custom form, for example, a search form
class ExampleForm(forms.Form):
    search_term = forms.CharField(max_length=200, required=True, label="Search Term")
