from django.urls import path
from . import views 
app_name = 'orders'


urlpatterns = [
    path('add/', views.add, name='add'),
    path('user_products', views.user_products, name= 'user_products'),
]
