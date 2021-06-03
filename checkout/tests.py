from django.test import TestCase, Client
from .forms import OrderForm
from .models import Order, OrderLineItem
from .views import mockingPubKey, mockingSecKey, checkout_receipt
from django.conf import settings
import uuid
from datetime import datetime


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


class TestOrderModel(TestCase):
    def create_fake_order(self,
                          order_number=uuid.uuid4().hex.upper(),
                          full_name="john obrien",
                          email="john@managemyweb.com",
                          phone_number="1234",
                          country="IE",
                          town_or_city="Dublin",
                          street_address1="test",
                          date=datetime.now(),
                          order_total=0.1,
                          tax=0.1,
                          grand_total=0.2,
                          subscription=False,
                          original_cart="{Test}",
                          stripe_pid=""):
        return Order.objects.create(order_number=order_number,
                                    full_name=full_name,
                                    email=email,
                                    phone_number=phone_number,
                                    country=country,
                                    town_or_city=town_or_city,
                                    street_address1=street_address1,
                                    date=date,
                                    order_total=order_total,
                                    tax=tax,
                                    grand_total=grand_total,
                                    subscription=subscription,
                                    original_cart=original_cart,
                                    stripe_pid=stripe_pid)

    def test_order_number(self):
        o = self.create_fake_order()
        self.assertTrue(isinstance(o, Order))
        self.assertEqual(str(o), str(o.order_number))
