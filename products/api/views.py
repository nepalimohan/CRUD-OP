from urllib import request
from django.shortcuts import render
from rest_framework.views import APIView
from products.api.serializers import ProductSerializer
from products.models import Product
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins


#creating product list using mixins and generics

class ProductList(mixins.ListModelMixin,
                  mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class ProductDetails(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def retireve(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
# Create your views here.
class ProductListAV(APIView):
    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProductSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class ProductDetailsAV(APIView):
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({'Error': 'Product not found'}, status= status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk):
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)