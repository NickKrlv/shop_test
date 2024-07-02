from rest_framework import serializers
from .models import Category, Subcategory, Product, Cart, CartItem


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    subcategory = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['name', 'slug', 'category', 'subcategory', 'price', 'image_small', 'image_medium', 'image_large']

    def get_category(self, obj):
        return obj.subcategory.category.name

    def get_subcategory(self, obj):
        return obj.subcategory.name


class SubcategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Subcategory
        fields = ['name', 'slug', 'category', 'image', 'products']


class SubcategorySimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['name', 'slug', 'category', 'image']


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubcategorySimpleSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['name', 'slug', 'image', 'subcategories']


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product', write_only=True)

    class Meta:
        model = CartItem
        fields = ['product', 'product_id', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    total_items = serializers.SerializerMethodField()
    total_cost = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['items', 'total_items', 'total_cost']

    def get_total_items(self, obj):
        return sum(item.quantity for item in obj.items.all())

    def get_total_cost(self, obj):
        return sum(item.quantity * item.product.price for item in obj.items.all())
