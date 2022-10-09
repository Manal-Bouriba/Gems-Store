from django.test import TestCase

# Create your tests here.
from django import urls
from django.urls import path
from .views import ProductList, ProductDetails


app_name='api'

urlpatterns = [
    path('product/',ProductList.as_view(),name='productlist'),
    path('product/<int:pk>/',ProductDetails.as_view(),name='productdetails'),



]