from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from shop.models import Category, Subcategory, Product


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        users = [
            {'username': 'user1', 'email': 'user1@example.com', 'password': 'password123'},
            {'username': 'user2', 'email': 'user2@example.com', 'password': 'password123'},
            {'username': 'user3', 'email': 'user3@example.com', 'password': 'password123'},
        ]

        for user_data in users:
            user, created = User.objects.get_or_create(username=user_data['username'], email=user_data['email'])
            if created:
                user.set_password(user_data['password'])
                user.save()
            self.stdout.write(self.style.SUCCESS(f'User "{user.username}" created'))

        categories = [
            {'name': 'Fruits', 'slug': 'fruits', 'image': 'path/to/fruits.jpg'},
            {'name': 'Vegetables', 'slug': 'vegetables', 'image': 'path/to/vegetables.jpg'},
            {'name': 'Dairy', 'slug': 'dairy', 'image': 'path/to/dairy.jpg'},
        ]

        for category_data in categories:
            category, created = Category.objects.get_or_create(
                name=category_data['name'], slug=category_data['slug'])
            if created:
                category.image.name = category_data['image']
                category.save()
            self.stdout.write(self.style.SUCCESS(f'Category "{category.name}" created'))

        subcategories = [
            {'name': 'Citrus', 'slug': 'citrus', 'category_name': 'Fruits', 'image': 'path/to/citrus.jpg'},
            {'name': 'Berries', 'slug': 'berries', 'category_name': 'Fruits', 'image': 'path/to/berries.jpg'},
            {'name': 'Leafy Greens', 'slug': 'leafy-greens', 'category_name': 'Vegetables',
             'image': 'path/to/leafy_greens.jpg'},
        ]

        for subcategory_data in subcategories:
            category = Category.objects.get(name=subcategory_data['category_name'])
            subcategory, created = Subcategory.objects.get_or_create(
                name=subcategory_data['name'], slug=subcategory_data['slug'], category=category)
            if created:
                subcategory.image.name = subcategory_data['image']
                subcategory.save()
            self.stdout.write(self.style.SUCCESS(f'Subcategory "{subcategory.name}" created'))

        products = [
            {'name': 'Orange', 'slug': 'orange', 'subcategory_name': 'Citrus', 'price': 0.5,
             'image_small': 'path/to/orange_small.jpg', 'image_medium': 'path/to/orange_medium.jpg',
             'image_large': 'path/to/orange_large.jpg'},
            {'name': 'Strawberry', 'slug': 'strawberry', 'subcategory_name': 'Berries', 'price': 1.0,
             'image_small': 'path/to/strawberry_small.jpg', 'image_medium': 'path/to/strawberry_medium.jpg',
             'image_large': 'path/to/strawberry_large.jpg'},
            {'name': 'Spinach', 'slug': 'spinach', 'subcategory_name': 'Leafy Greens', 'price': 2.5,
             'image_small': 'path/to/spinach_small.jpg', 'image_medium': 'path/to/spinach_medium.jpg',
             'image_large': 'path/to/spinach_large.jpg'},
        ]

        for product_data in products:
            subcategory = Subcategory.objects.get(name=product_data['subcategory_name'])
            product, created = Product.objects.get_or_create(
                name=product_data['name'], slug=product_data['slug'], subcategory=subcategory,
                price=product_data['price'])
            if created:
                product.image_small.name = product_data['image_small']
                product.image_medium.name = product_data['image_medium']
                product.image_large.name = product_data['image_large']
                product.save()
            self.stdout.write(self.style.SUCCESS(f'Product "{product.name}" created'))

        self.stdout.write(self.style.SUCCESS('Database successfully seeded'))
