# Generated by Django 3.2 on 2021-04-20 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20210420_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='plan',
            field=models.BooleanField(default=False),
        ),
    ]
