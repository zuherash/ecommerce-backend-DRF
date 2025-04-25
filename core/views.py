from django.shortcuts import render
from rest_framework import generics,permissions
from .models import Product
from .serializers import ProductSerializer

class productlistcreateview(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes=[permissions.IsAuthenticated]
    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)
    
    
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)
        
class ProductRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class =ProductSerializer
    

