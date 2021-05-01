from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total', "subscription")


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
    readonly_fields = ("order_number", "date", "subscription", "tax",
                       "order_total", "grand_total", "subscriber",
                       "original_cart", "stripe_pid",)
    fields = ("order_number", "date", "full_name",
              "email", "phone_number", "country",
              "postcode", "town_or_city", "street_address1",
              "street_address2", "order_total", "tax",
              "grand_total", "subscription", "subscriber",
              "original_cart", "stripe_pid",)
    list_display = ("order_number", "date", "full_name",
                    "subscriber", "order_total", "grand_total",)
    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
