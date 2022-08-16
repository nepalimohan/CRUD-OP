from django.shortcuts import render
from rest_framework.views import APIView
from products.api.serializers import ProductSerializer
from products.models import Product
from rest_framework.response import Response

# Create your views here.
class ProductListAV(APIView):
    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)
    
    # def post(self, request):
    #     serializer = ProductSerializer(data=request.data)
    #     if serializer.is_valid():
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors)