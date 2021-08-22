from django.contrib import admin
from .models import Product, Category, ParentCategory


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "price",
        "plan",
        "on_sale",
        "sold",
        "available",
        "image1",
        "add_date",
        "rating_update",
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "parent_category",
        "friendly_name",
        "name",
    )


class ParentCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name",
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ParentCategory, ParentCategoryAdmin)
