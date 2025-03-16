from django.contrib import admin

from .models import Book  # Import the Book model

# Customize the admin interface for the Book model
class BookAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ('title', 'author', 'published_year')

    # Enable search functionality for the 'title' and 'author' fields
    search_fields = ('title', 'author')

    # Add filters for the 'published_year'
    list_filter = ('published_year',)


    def publication_year(self, obj):
        return obj.published_year.year if obj.published_year else None

    publication_year.admin_order_field = 'published_year'  # Sort by the published year
    publication_year.short_description = 'Publication Year'

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

# Step 2: Create and Configure Groups with Assigned Permissions

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


def create_groups_and_permissions():
    content_type = ContentType.objects.get_for_model(Book)

    # Define permissions
    permissions = {
        "can_view": "Can view book",
        "can_create": "Can create book",
        "can_edit": "Can edit book",
        "can_delete": "Can delete book",
    }

    # Create or get permissions
    for codename, name in permissions.items():
        Permission.objects.get_or_create(codename=codename, name=name, content_type=content_type)

    # Define groups and assign permissions
    groups_permissions = {
        "Viewers": ["can_view"],
        "Editors": ["can_view", "can_create", "can_edit"],
        "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
    }

    for group_name, perms in groups_permissions.items():
        group, created = Group.objects.get_or_create(name=group_name)
        for perm in perms:
            permission = Permission.objects.get(codename=perm, content_type=content_type)
            group.permissions.add(permission)

# Run function to create groups and assign permissions
create_groups_and_permissions()
