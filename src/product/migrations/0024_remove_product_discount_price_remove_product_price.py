# Generated by Django 4.2 on 2023-07-20 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0023_product_version_discount_price_product_version_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='discount_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
    ]
