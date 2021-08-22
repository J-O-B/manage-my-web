from django.test import TestCase


class URLTests(TestCase):
    # Url Test
    def test_main_products(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
