from django.shortcuts import render

from .utils import get_or_create_cart

from .models import Cart
from Tienda_online.models import Product

def cart(request):
    
    cart = get_or_create_cart(request)
   
    return render(request,'carts/carts.html',{
    'cart':cart
})

def add(request):
    cart = get_or_create_cart(request)
    product = Product.objects.get(pk=request.POST.get('product_id'))

    cart.products.add(product)

    return render(request, 'carts/add.html',{
        'product': product
    })
