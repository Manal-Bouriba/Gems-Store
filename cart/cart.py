from store.models import Product
from decimal import Decimal

class Cart():
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('skey')
        if 'skey' not in request.session:
            cart = self.session['skey'] = {}
        self.cart = cart

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        
        
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            yield item 

    def add(self, product):
        product_id = product.id
        if product_id not in self.cart:
            self.cart[product_id] = {'price': str(product.price)}
        self.session.modified = True    

    def get_total_price(self):
        return sum(Decimal(item['price']) for item in self.cart.values())

    def delete(self, product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
        self.session.modified = True