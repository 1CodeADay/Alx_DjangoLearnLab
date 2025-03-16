# Permissions and Groups in Bookshelf App

## Custom Permissions
- `can_view`: Can view books.
- `can_create`: Can create books.
- `can_edit`: Can edit books.
- `can_delete`: Can delete books.

## User Groups
- **Viewers**: Can only view books.
- **Editors**: Can view, create, and edit books.
- **Admins**: Full access (view, create, edit, delete).

## Setup
Run the following commands:

python manage.py makemigrations bookshelf python manage.py migrate python manage.py shell

from bookshelf.admin import create_groups_and_permissions create_groups_and_permissions()
