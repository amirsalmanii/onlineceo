from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import User as CustomUser
from .forms import UserCreationForm, UserChangeForm


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    form_add = UserCreationForm
    list_display = (
        "username",
        "first_name",
        "last_name",
        "is_admin",
        "is_operator",
    )
    list_filter = ("is_admin",)
    search_fields = ("email", "username")
    # list_editable

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "email",
                    "first_name",
                    "last_name",
                    "avatar",
                    "password",
                    "state",
                    "city",
                    "address",
                    "plate",
                    "zip_code",
                    "wallet",
                )
            },
        ),
        ("Personal Info", {"fields": ("is_active",)}),
        ("Personal Perms", {"fields": ("is_admin",)}),
    )

    add_fieldsets = ((None, {"fields": ("username", "password1", "password2")}),)

    ordering = ("-id",)
    filter_horizontal = ()


admin.site.register(CustomUser, UserAdmin)
admin.site.unregister(Group)