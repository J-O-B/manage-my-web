from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django_countries.fields import CountryField

from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(
        max_length=50, null=True, blank=True)
    email = models.EmailField(
        max_length=254, null=True, blank=True)
    phone_number = models.CharField(
        max_length=20, null=True, blank=True)
    country = CountryField(
        blank_label="Country *", null=True, blank=True)
    postcode = models.CharField(
        max_length=20, null=True, blank=True)
    town_or_city = models.CharField(
        max_length=40, null=True, blank=True)
    street_address1 = models.CharField(
        max_length=80, null=True, blank=True)
    street_address2 = models.CharField(
        max_length=80, null=True, blank=True)
    subscription = models.BooleanField(
        default=False, null=True, editable=False)
    subscription_expiry = models.DateField(
        default=datetime.now(), null=True, blank=True)

    def __str__(self):
        return str(self.user.username)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    # Create or update the user profile
    if created:
        UserProfile.objects.create(user=instance)
    # Existing Users
    instance.userprofile.save()
