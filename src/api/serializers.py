from rest_framework import serializers 
from order.models import wishlist, basket, basket_item, order
from product.models import Size, Category, Color, Manufacturer, Product, Product_version 
from users.models import User 

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields=[
            'name'
        ]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'is_main',
            'p_category'
        ]

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = [
            'name'
        ]
class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = [ 
            'name'
        ]


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer
    manufacturer = ManufacturerSerializer

    class Meta:
        model = Product
        fields = [
            'name',
            'price',
            'discount_price',
            'in_sale',
            'category',
            'description',
            'manufacturer'
        ]


class ProductVersionSerializer(serializers.ModelSerializer):
    color = ColorSerializer
    product = ProductSerializer
    size = SizeSerializer

    class Meta:
        model = Product_version
        fields = [
            'id',
            'read_count',
            'cover_image',
            'color',
            'product',
            'size',
            'units_sold'
        ]