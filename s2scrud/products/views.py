
from rest_framework import renderers, viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Attribute
from . import serializers


# Create your views here.


class ProductListView(viewsets.ModelViewSet):
    serializer_class = serializers.ProductSerializer
    queryset = Product.objects.all()
    renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer)

    def list(self, request, *args, **kwargs):

        response = super(ProductListView, self).list(request, *args, **kwargs)
        if request.accepted_renderer.format == 'html':
            return Response({'data': response.data}, template_name='products/products.html')
        return response

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            attribute = serializer.validated_data.get('attribute')
            sku = serializer.validated_data.get('sku')

            attribute = Attribute.objects.create(**attribute)
            product = Product.objects.create(sku=sku, attribute_id=attribute.id)

            return Response(
                serializer.validated_data, status=status.HTTP_201_CREATED
            )

        else:
            return Response(serializer.validated_data, status=status.HTTP_400_BAD_REQUEST)

class ProductCreateView(viewsets.ModelViewSet):
    serializer_class = serializers.ProductSerializer
    queryset = Product.objects.all()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            attribute = serializer.validated_data.get('attribute')
            sku = serializer.validated_data.get('sku')

            attribute = Attribute.objects.create(**attribute)
            product = Product.objects.create(sku=sku, attribute_id=attribute.id)

            return Response(
                serializer.validated_data, status=status.HTTP_201_CREATED
            )

        else:
            return Response(serializer.validated_data, status=status.HTTP_400_BAD_REQUEST)
