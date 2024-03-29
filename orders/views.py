from django.http.response import JsonResponse
from django.shortcuts import render

from cart.cart import Cart

from .models import Order, OrderItem


def add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':

        order_key = request.POST.get('order_key')
        user_id = request.user.id
        carttotal = cart.get_total_price()

        # Check if order exists
        if Order.objects.filter(order_key=order_key).exists():
            pass
        else:
            order = Order.objects.create(user_id=user_id, 
                                 total_paid=carttotal, order_key=order_key)
            order_id = order.pk

            for item in cart:
                OrderItem.objects.create(order_id=order_id, product=item['product'], price=item['price'])

        response = JsonResponse({'success': 'Return something'})
        return response


def payment_confirmation(data):
    Order.objects.filter(order_key=data).update(billing_status=True)


def user_products(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id).filter(billing_status=True)
    orderitems = OrderItem.objects.all()
    products = []
    for product in orderitems:
        for item in orders:
            if product.order.id == item.id:
                products.append(product)
                break
    return render(request, 'store/user_products.html', {'products': products})
