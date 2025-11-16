from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, CustomUser

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # columns shown in list view
    list_filter = ('publication_year', 'author')            # sidebar filters
    search_fields = ('title', 'author')                     # search bar


class CustomUserAdmin(UserAdmin):
    """
    Custom admin panel for the CustomUser model,
    including the additional fields: date_of_birth and profile_photo.
    """

    model = CustomUser

    # Fields visible in the admin list view
    list_display = ("email", "date_of_birth", "is_staff", "is_superuser")
    list_filter = ("is_staff", "is_superuser", "date_of_birth")

    # Field layout when editing an existing user
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Information", {"fields": ("date_of_birth", "profile_photo")}),
        ("Permissions", {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            )
        }),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
    )

    # Field layout when adding a new user
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email",
                "password1",
                "password2",
                "date_of_birth",
                "profile_photo",
                "is_staff",
                "is_superuser",
            ),
        }),
    )

    search_fields = ("email",)
    ordering = ("email",)

admin.site.register(CustomUser, CustomUserAdmin)
