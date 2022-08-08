from rest_framework import serializers
from .models import Category, Product, Book

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'title'
        )
        model = Category

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'title',
            'category',
            'isbn',
            'pages',
            'price',
            'stock',
            'description', 
            'imageUrl',
            'status',
            'date_created',

        )
        model = Book

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = (
            'id',
            'product_id',
            'name',
            'category'
            'price',
            'stock',
            'description', 
            'imageUrl',
            'status',
            'date_created',
        )
        model = Product