from django.contrib import admin

from .models import Category, Developer, Franchise, ProductScreenshot, Publisher
from .models import Product

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Developer)
admin.site.register(Publisher)
admin.site.register(Franchise)
admin.site.register(ProductScreenshot)