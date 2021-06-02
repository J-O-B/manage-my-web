from django.test import TestCase, Client
from .forms import OrderForm
from .models import Order
from .views import mockingPubKey, mockingSecKey, checkout_receipt
from django.conf import settings


# Test Checkout Form
class CheckoutTests(TestCase):
    def test_order_form_Meta(self):
        form = OrderForm()
        self.assertEqual(form.Meta.model, Order)

    def test_order_form_fields(self):
        form = OrderForm()
        testFields = ("full_name", "email", "phone_number",
                      "street_address1", "street_address2",
                      "town_or_city", "postcode", "country",
                      "subscription",)
        self.assertEqual(form.Meta.fields, testFields)

    def test_pub_key(self):
        key = mockingPubKey()
        self.assertEqual(settings.STRIPE_PUBLIC_KEY, key)

    def test_sec_key(self):
        key = mockingSecKey()
        self.assertEqual(settings.STRIPE_SECRET_KEY, key)
