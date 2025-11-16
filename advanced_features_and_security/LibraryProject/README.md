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


# Security Features Implemented

## 1. Django Secure Settings
- DEBUG = False (production)
- SECURE_BROWSER_XSS_FILTER enabled to prevent reflected XSS
- X_FRAME_OPTIONS = DENY to prevent clickjacking
- SECURE_CONTENT_TYPE_NOSNIFF enabled to prevent MIME sniffing
- SESSION_COOKIE_SECURE and CSRF_COOKIE_SECURE ensure cookie transmission only over HTTPS

## 2. CSRF Protection
All forms use {% csrf_token %} to prevent CSRF attacks.

## 3. Secure Views and Data Handling
- ORM is used instead of raw SQL to avoid SQL injection
- User input is validated through Django forms
- Queries use parameterized ORM calls (safe by default)

## 4. Content Security Policy (CSP)
Configured via django-csp middleware to limit allowed content sources and reduce XSS risk.

## 5. Manual Testing Performed
- Attempted form submission without CSRF token (Django blocked)
- Attempted SQL injection-like payloads in search fields (Django ORM sanitized them)
- Tested views using multiple roles and permissions
