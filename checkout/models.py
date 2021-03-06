from django.db import models
from django.db.models import Sum
from django.conf import settings

from products.models import Product
from profiles.models import UserProfile

import uuid
from django_countries.fields import CountryField


class Order(models.Model):

    order_number = models.CharField(
        max_length=32, null=False, editable=False)

    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL, null=True,
        blank=True, related_name='orders')

    full_name = models.CharField(
        max_length=50, null=False, blank=False)

    email = models.EmailField(
        max_length=254, null=False, blank=False)

    phone_number = models.CharField(
        max_length=20, null=False, blank=False)

    country = CountryField(
        blank_label="Country *", null=False, blank=False)

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

    subscription = models.BooleanField(default=False, null=True, editable=True)

    subscriber = models.CharField(max_length=3, null=True, default="No", editable=True)

    original_cart = models.TextField(null=False, blank=False, default='')

    stripe_pid = models.CharField(max_length=512, null=False, blank=False, default='')

    def _generate_order_number(self):
        # Generate a random, unique order number using UUID
        return uuid.uuid4().hex.upper()

    def update_order(self):
        line_items = OrderLineItem.objects.filter(order=self.id)
        # Update grand total each time a line item is added, accounting for tax
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.grand_total = self.order_total + (
            self.order_total * settings.TAX_PERCENTAGE / 100)
        self.tax = self.order_total * settings.TAX_PERCENTAGE / 100
        self.save()

    def save(self, *args, **kwargs):
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
    subscription = models.BooleanField(null=True)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2,
        null=False, blank=False, editable=False)
    delivered = models.DateField(null=True, blank=True)
    website = models.CharField(max_length=32, null=True, editable=False)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2,
        null=True, blank=True)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        if self.product.plan == 2:
            self.subscription = True
        else:
            self.subscription = False
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        string = f'Product: {self.product.name} on order \
            {self.order.order_number}'
        return string