from django.shortcuts import render
from .utils import get_or_create_order
from carts.utils import get_or_create_cart
from .utils import breadcrumb

from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def order(request):
    
    cart = get_or_create_cart(request)
    order = get_or_create_order(cart, request)

    return render(request, 'orders/order.html',{
        'cart': cart,
        'order': order,
        'breadcrumb': breadcrumb(),
    })
