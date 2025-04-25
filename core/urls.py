from django.urls import path
from .views import productlistcreateview,ProductRetriveUpdateDestroyView

urlpatterns = [
    path("products/", productlistcreateview.as_view(), name="product-list-create"),
    path("products/int:<pk>", ProductRetriveUpdateDestroyView.as_view(), name="product_detail")
    
]
