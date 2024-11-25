from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from utils.base_utils import get_model

User = get_model(app_name="accounts", model_name="User")
Otp = get_model(app_name="accounts", model_name="Otp")


@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            "Other Info",
            {
                "fields": (
                    "image",
                    "age",
                    "phone_number",
                    "account_verified",
                    "gender",
                )
            },
        ),
    )
    list_display = (
        "username",
        "email",
        "age",
        "phone_number",
        "account_verified",
        "gender",
    )
    list_filter = (
        "account_verified",
        "gender",
    )
    search_fields = (
        "username",
        "email",
        "phone_number",
    )
    readonly_fields = ("created", "modified")


@admin.register(Otp)
class OtpAdmin(admin.ModelAdmin):
    """Otp Admin"""

    list_display = ("user", "otp", "created", "expiry")
    list_filter = ("created", "expiry")
    search_fields = ("otp",)
    readonly_fields = ("created", "expiry")
