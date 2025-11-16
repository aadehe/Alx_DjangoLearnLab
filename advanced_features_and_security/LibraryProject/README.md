# Introduction to Django

# Permissions and Groups Setup

This app implements Django's permission and group system to control access.

## Custom Permissions
Defined in Article model (models.py):
- can_view  → view articles
- can_create → create new articles
- can_edit  → modify existing articles
- can_delete → delete articles

## Groups Created
- Viewers → can_view
- Editors → can_view, can_create, can_edit
- Admins  → can_view, can_create, can_edit, can_delete

## Enforcement in Views
Views use @permission_required to restrict actions:
- article_list    → can_view
- article_create  → can_create
- article_edit    → can_edit
- article_delete  → can_delete

Assign users to groups via Django Admin or using the command:
python manage.py create_groups
