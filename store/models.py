from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse



class Category(models.Model):
    title =models.CharField(max_length=255)
    slug =models.SlugField(max_length=255)
    
    class Meta:
        verbose_name_plural ="Categories"
        
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])    

class Developer(models.Model):
    title=models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Publisher(models.Model):
    title=models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Franchise(models.Model):
    title = models.CharField(max_length=255)  
    def __str__(self):
        return self.title 


class Product(models.Model):
    title = models.CharField(max_length=255)  
    id = models.BigAutoField(primary_key=True)
    slug = models.SlugField(max_length=255)
    price = models.FloatField(null=True)
    picture = models.ImageField(null=True)
    featurepic = models.ImageField(null=True, blank=True)
    franchise =models.ForeignKey(Franchise,related_name='products',on_delete=models.SET_NULL,null=True, blank=True)
    category =models.ForeignKey(Category,related_name='products',on_delete=models.SET_NULL,null=True)
    developer = models.ForeignKey(Developer, on_delete=models.SET_NULL, null=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True)
    platform = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)  
    featured = models.BooleanField()
    popular = models.BooleanField()
    platform = models.TextField()
    def get_absolute_url(self):
        return reverse('store:product_details', args=[self.slug])
    
    def __str__(self):
        return self.title 
     
     
class ProductScreenshot(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')
 
    def __str__(self):
        return self.product.title

