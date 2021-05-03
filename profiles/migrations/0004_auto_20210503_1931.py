# Generated by Django 3.2 on 2021-05-03 19:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20210503_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='subscription',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='subscription_expiry',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 5, 3, 19, 31, 24, 559562), null=True),
        ),
    ]