# Generated by Django 3.2 on 2021-04-21 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20210421_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='product',
            name='rating_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]