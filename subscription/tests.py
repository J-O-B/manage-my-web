from django.test import TestCase
from django.shortcuts import reverse


class CheckSubscriptions(TestCase):
    # Url Test
    def test_root_url(self):
        url = reverse('subscription')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_gold_url(self):
        url = reverse('gold')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_silver_url(self):
        url = reverse('silver')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
