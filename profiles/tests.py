from django.test import TestCase
from .forms import UserProfileForm
from .models import UserProfile
# Create your tests here.


class TestForm(TestCase):
    def testFields(self):
        fields = UserProfileForm.Meta.fields
        test_fields = ("full_name", "email", "phone_number",
                       "street_address1", "street_address2",
                       "town_or_city", "postcode", "country",)
        self.assertEqual(fields, test_fields)

    def testModel(self):
        model = UserProfileForm.Meta.model
        test_model = UserProfile
        self.assertEqual(model, test_model)

    def testWidget(self):
        form = UserProfileForm()
        statement = form.fields['full_name'].widget.attrs['autofocus']
        self.assertEqual(statement, True)

    def testPlaceholder(self):
        form = UserProfileForm()
        placeholders = {
            "full_name": "Full Name",
            "email": "Email Address",
            "phone_number": "Phone Number",
            "town_or_city": "City",
            "street_address1": "Address Line 1",
            "street_address2": "Address Line 2",
            "postcode": "Post Code",
            "subscription": "subscription",
        }
        for field in form.fields:
            if field == 'full_name':
                placeholder = f'{placeholders[field]} *'
        wanted_output = "Full Name *"
        self.assertEqual(wanted_output, placeholder)
