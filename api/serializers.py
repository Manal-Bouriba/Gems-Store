from django.db import models

# Create your models here.
from django.db.models import fields
from rest_framework import serializers

from store.models import Product,Category,Developer,Publisher,Franchise,ProductScreenshot



class Productserializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields = ('id','title','price','picture','featurepic','franchise',
        'category','developer','publisher','platform','description')


class Categoryserializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields=('title')     