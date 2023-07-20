# Generated by Django 4.2 on 2023-07-20 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0020_alter_product_version_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_version',
            name='price',
            field=models.DecimalField(decimal_places=2, help_text='The regular price of the product', max_digits=8),
        ),
    ]
