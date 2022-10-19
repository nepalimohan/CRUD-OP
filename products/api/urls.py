from django.urls import path
from products.api.views import ProductList, ProductDetailsGV, ProductListGV

urlpatterns = [
    path('list/', ProductListGV.as_view(), name='product-list'),
    path('<int:pk>/', ProductDetailsGV.as_view(), name='product-details'),
]
