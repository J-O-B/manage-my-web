from django.test import TestCase
from django.shortcuts import reverse


class TestAbout(TestCase):
    # Test the About Page URL & Template
    def test_abut_page(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about/about.html')
