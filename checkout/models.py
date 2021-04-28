from django.db import models
from django.db.models import Sum
from django.conf import settings

from products.models import Product
import uuid
from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.utils import timezone


class Order(models.Model):

    order_number = models.CharField(
        max_length=32, null=False, editable=False)

    full_name = models.CharField(
        max_length=50, null=False, blank=False)

    email = models.EmailField(
        max_length=254, null=False, blank=False)

    phone_number = models.CharField(
        max_length=20, null=False, blank=False)

    country = models.CharField(
        max_length=40, null=False, blank=False)

    postcode = models.CharField(
        max_length=20, null=True, blank=True)

    town_or_city = models.CharField(
        max_length=40, null=False, blank=False)

    street_address1 = models.CharField(
        max_length=80, null=False, blank=False)

    street_address2 = models.CharField(
        max_length=80, null=True, blank=True)

    date = models.DateTimeField(
        auto_now_add=True)

    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)

    tax = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)

    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)

    subscription = models.BooleanField(default=False, null=False)

    def _generate_order_number(self):
        # Generate a random, unique order number using UUID
        return uuid.uuid4().hex.upper()

    def update_total(self):
        # Update grand total each time a line item is added, accounting for tax
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.order_total > 0:
            self.grand_total = self.order_total + (
                self.order_total * settings.TAX_PERCENTAGE / 100)
            self.tax = self.order_total * settings.TAX_PERCENTAGE / 100
        else:
            self.order_total = 0
            self.grand_total = 0
            self.tax = 0
        self.save()

    def save(self, *args, **kwargs):
        # Override the original save method
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.order_number)


class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2,
        null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Product: {self.product.name} on order \
            {self.order.order_number}'
