from rest_framework import serializers
from .models import Brand ,Category,Product


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'name')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name', 'parent_category', 'date_created', 'last_modified')


class ProductSerializer(serializers.ModelSerializer):
    specification = serializers.JSONField()
    class Meta:
        model = Product
        fields = ('id', 'name', 'specification',) 