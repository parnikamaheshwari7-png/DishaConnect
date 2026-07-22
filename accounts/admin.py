from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, GuideProfile, Expertise


admin.site.register(GuideProfile)
admin.site.register(Expertise)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):

    model = CustomUser

    list_display = (
        "email",
        "first_name",
        "last_name",
        "role",
        "approval_status",
        "is_approved",
        "is_staff",
    )

    list_filter = (
        "role",
        "approval_status",
        "is_approved",
        "is_staff",
    )

    ordering = ("email",)

    search_fields = (
        "email",
        "first_name",
        "last_name",
    )

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                )
            },
        ),

        (
            "Personal Information",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "mobile_number",
                )
            },
        ),

        (
            "Preferences",
            {
                "fields": (
                    "preferred_language",
                    "preferred_theme",
                )
            },
        ),

        (
            "Permissions",
            {
                "fields": (
                    "role",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),

        (
            "Guide Approval",
            {
                "fields": (
                    "is_verified",
                    "is_approved",
                    "approval_status",
                    "approved_by",
                    "approved_at",
                    "rejection_reason",
                )
            },
        ),

        (
            "Important Dates",
            {
                "fields": (
                    "last_login",
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )

    readonly_fields = (
        "created_at",
        "updated_at",
        "last_login",
        "approved_at",
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "first_name",
                    "last_name",
                    "role",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )