# Generated by Django 3.2 on 2021-04-27 16:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0008_auto_20210427_1559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlineitem',
            name='expiry',
        ),
        migrations.RemoveField(
            model_name='orderlineitem',
            name='subscription',
        ),
        migrations.AlterField(
            model_name='order',
            name='expiry',
            field=models.DateField(default=datetime.datetime(2021, 4, 27, 16, 5, 6, 895431)),
        ),
    ]
