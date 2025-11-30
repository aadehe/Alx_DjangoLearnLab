# Advanced API Project — Custom and Generic Views

## Overview
This project demonstrates how to use Django REST Framework’s generic views and mixins to build efficient CRUD endpoints with minimal boilerplate. It includes custom behavior, permissions, filters, and nested serialization.

---

## Views

### BookListView
- **Endpoint:** GET `/api/books/`
- **Purpose:** List all books
- **Access:** Public (AllowAny)

### BookDetailView
- **Endpoint:** GET `/api/books/<pk>/`
- **Purpose:** Retrieve single book
- **Access:** Public (AllowAny)

### BookCreateView
- **Endpoint:** POST `/api/books/create/`
- **Purpose:** Create new book
- **Access:** Authenticated users only
- **Custom Logic:** Uses `perform_create` hook

### BookUpdateView
- **Endpoint:** PUT/PATCH `/api/books/<pk>/update/`
- **Purpose:** Update existing book
- **Access:** Authenticated only
- **Custom Logic:** Uses `perform_update` hook

### BookDeleteView
- **Endpoint:** DELETE `/api/books/<pk>/delete/`
- **Purpose:** Delete a book
- **Access:** Authenticated only

---

## Permissions
- Read-only endpoints are public.
- Create/Update/Delete require authentication (`IsAuthenticated`).

---

## Customizations
- Hooks (`perform_create`, `perform_update`)
- Optional query filtering in `get_queryset()`
- DRF serializers provide automatic validation, including custom rules.

---
# Filtering, Searching, and Ordering

The API supports flexible and powerful querying on the `/api/books/` endpoint.

## Filtering
Filtering uses DRF’s DjangoFilterBackend.  
Available filter fields:
- `title`
- `publication_year`
- `author`

Example:
``/api/books/?title=Foundation&publication_year=1951``  


## Searching
Searching uses DRF’s SearchFilter.  
Searches across:
- `title`
- `author` name

Example:
``/api/books/?search=asimov``  


## Ordering
Ordering uses DRF’s OrderingFilter.  
Supported fields:
- `title`
- `publication_year`

Examples:  
``/api/books/?ordering=title``  
``/api/books/?ordering=-publication_year``  


## Combined Example
``/api/books/?search=robot&author=1&ordering=-publication_year``  


These features are implemented in `BookListView` using DRF’s filter backends.


---

## Testing
Use **Postman**, **curl**, or Django’s admin and shell to verify expected behavior and permission restrictions.
