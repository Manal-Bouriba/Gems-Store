from django.urls import path
from store.views import *


app_name = 'store'

urlpatterns = [
path('',home, name='home'),
path('game/<slug:slug>', product_detail, name='product_details'),
path('category/<slug:category_slug>/', category_list, name='category_list'),
]  
  
