from django.db import models


class LeadGen(models.Model):
    class Meta:
        verbose_name_plural = "Lead Generation"
    # Track User Requests Via Contact Form

    full_name = models.CharField(
        max_length=50, null=False, blank=False)

    email = models.EmailField(
        max_length=254, null=False, blank=False)

    subject = models.CharField(
        max_length=75, null=False, blank=False)

    message = models.TextField(
        max_length=1024, null=False, blank=False)

    date = models.DateField(
        auto_now=True, blank=False, null=False)

    def __str__(self):
        return str(self.full_name)


class EmailMarketing(models.Model):
    class Meta:
        verbose_name_plural = "Marketing List"

    users_name = models.CharField(
        max_length=50, null=False, blank=False)

    email = models.EmailField(
        max_length=254, null=False, blank=False)

    category = models.CharField(
        max_length=50, null=False, blank=False)

    def __str__(self):
        return str(self.users_name)
