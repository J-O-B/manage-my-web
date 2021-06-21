from django.contrib import admin
from .models import LeadGen, EmailMarketing


class LeadAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "subject", "message", "date")
    ordering = ('date',)


class EmailAdmin(admin.ModelAdmin):
    list_display = ("users_name", "email", "category")
    ordering = ('users_name',)


admin.site.register(LeadGen, LeadAdmin)
admin.site.register(EmailMarketing, EmailAdmin)