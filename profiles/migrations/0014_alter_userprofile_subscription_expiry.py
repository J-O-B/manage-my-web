# Generated by Django 3.2 on 2021-06-14 22:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0013_alter_userprofile_subscription_expiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='subscription_expiry',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 6, 14, 22, 49, 55, 339864), null=True),
        ),
    ]
