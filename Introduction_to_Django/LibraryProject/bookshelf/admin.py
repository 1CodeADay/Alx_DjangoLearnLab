from django.contrib import admin

from .models import Book  # Import the Book model

# Customize the admin interface for the Book model
class BookAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ('title', 'author', 'publication_year')

    # Enable search functionality for the 'title' and 'author' fields
    search_fields = ('title', 'author')

    # Add filters for the 'publication_year'
    list_filter = ('publication_year',)

# Register the Book model with custom admin options
admin.site.register(Book, BookAdmin)
