# Generated by Django 3.1.7 on 2021-07-01 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_product_preview_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='has_upsell',
            field=models.IntegerField(choices=[(1, 'No'), (2, 'Yes')], default=1),
        ),
        migrations.AddField(
            model_name='product',
            name='upsell_target',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product'),
        ),
    ]
