from django.urls import path
from products.api.views import ProductListAV

urlpatterns = [
    path('list/', ProductListAV.as_view(), name='product-list'),
]
