from django.test import RequestFactory, TestCase
from .views import all_products
from django.shortcuts import reverse


class URLTests(TestCase):
    # Url Test
    def test_main_products(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

