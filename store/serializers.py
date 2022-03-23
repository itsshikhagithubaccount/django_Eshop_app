from rest_framework import serializers
from .models.product import Post1,Product
from .models.orders import Order
from .models.customer import Customer
from .models.category import Category
from .models.pagination import Post



class Post1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Post1
        fields = (
            'title',
            'description',
            'owner'
        )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


