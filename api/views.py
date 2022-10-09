from django.shortcuts import render
from rest_framework import generics

from store.models import Product,Category,Developer,Publisher,Franchise,ProductScreenshot
from .serializers import Productserializer



class ProductList(generics.ListAPIView):

    queryset= Product.objects.afrom django.shortcuts import render
from rest_framework import generics

from store.models import Product,Category,Developer,Publisher,Franchise,ProductScreenshot
from .serializers import Productserializer



class ProductList(generics.ListAPIView):

    queryset= Product.objects.all()
    serializer_class= Productserializer

    pass



class ProductDetails(generics.RetrieveAPIView):
    queryset= Product.objects.all()
    serializer_class= Productserializer


    pass