
from django.shortcuts import render, get_object_or_404
from store.models import Category, Product


def home(request):
    newest = Product.objects.all().order_by('-id')[:5]
    featuredgames = Product.objects.all().filter(featured= True)[:4]
    populargames = Product.objects.all().filter(popular = True)[:5]
    return render(request, 'home.html', {'products': newest, 'featuredgames' : featuredgames, 'populargames' : populargames})

def categories(request):
    return  {
        'categories': Category.objects.all() 
        
    }

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    franchise = Product.objects.all().filter(franchise= product.franchise)
    return render(request, 'store/product.html', {'product': product, 'franchise': franchise})

def category_list(request, category_slug):
    category= get_object_or_404(Category, slug=category_slug)
    productcat= Product.objects.filter(category = category)
    return render(request, 'store/category.html', {'category': category, 'productcat': productcat})

