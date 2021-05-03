from django.contrib import admin
from .models import UserProfile


class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ("subscription",)
    list_display = (
        "full_name",
        "phone_number",
        "email",
        "country",
        "subscription",
        "subscription_expiry",
        "created",
    )

    ordering = ('subscription_expiry',)


admin.site.register(UserProfile, ProfileAdmin)
