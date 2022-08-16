from django.urls import path
from products.api.views import ProductListAV, ProductDetailsAV

urlpatterns = [
    path('list/', ProductListAV.as_view(), name='product-list'),
    path('<int:pk>/', ProductDetailsAV.as_view(), name='product-details'),
]
