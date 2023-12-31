# Generated by Django 4.2 on 2023-04-08 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_remove_product_created_at_remove_product_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_main',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='category',
            name='p_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_category', to='product.category'),
        ),
    ]
