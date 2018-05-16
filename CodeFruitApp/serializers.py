from rest_framework import serializers

from CodeFruitApp.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'created', 'name', 'describe', 'price', 'isDelete')