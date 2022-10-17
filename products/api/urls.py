from django.urls import path
from products.api.views import ProductListAV, ProductDetailsAV, ProductList, ProductDetails

urlpatterns = [
    path('list/', ProductList.as_view(), name='product-list'),
    path('<int:pk>/', ProductDetails.as_view(), name='product-details'),
]
