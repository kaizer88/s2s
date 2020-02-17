from rest_framework import  serializers
from .models import Attribute, Product


class AttributeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attribute
        fields = ['id', 'size', 'grams', 'foo']


class ProductSerializer(serializers.Serializer):

    sku = serializers.CharField(max_length=5)
    attribute = AttributeSerializer(required=False)

    class Meta:
        model = Product
        fields = ('id','sku', 'attribute')
        read_only_fields = ('attribute',)
