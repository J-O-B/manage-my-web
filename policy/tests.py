from django.test import TestCase
from django.shortcuts import reverse


class URLTests(TestCase):
    # Url Test
    def test_root_url(self):
        url = reverse('policy')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)