from django.test import TestCase
from .models import Product


class URLTests(TestCase):
    # Url Test
    def test_main_products(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
