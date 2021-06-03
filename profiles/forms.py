from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("full_name", "email", "phone_number",
                  "street_address1", "street_address2",
                  "town_or_city", "postcode", "country",)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto generated
        labels and set autofocus to first field
        """
        super().__init__(*args, **kwargs)
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

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder

