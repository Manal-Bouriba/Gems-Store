from django.shortcuts import get_object_or_404, render
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
def cart_summary(request):
    cart = Cart(request)
    return render(request, 'cart/cart.html', {'cart': cart})

@csrf_exempt
def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product = product)
        response = JsonResponse({'test': 'data'})
        return response

@csrf_exempt
def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        cart.delete(product = product_id)
        carttotal = cart.get_total_price()
        response = JsonResponse({'Success': True, 'subtotal': carttotal})
        return response
