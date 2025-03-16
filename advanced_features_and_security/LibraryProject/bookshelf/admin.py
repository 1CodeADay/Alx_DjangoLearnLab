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


from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'date_of_birth', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
