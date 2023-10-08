from .models import Cart

def get_or_create_cart(request):
    user = request.user if request.user.is_authenticated else None
    cart_id = request.session.get('cart_id') #Retorna un NONE en el caso de que la llave no exista
    cart = Cart.objects.filter(cart_id=cart_id).first()  #None

    if cart is None:
        cart = Cart.objects.create(user=user)
    if user and cart.user is None:
        cart.user = user
        cart.save()

    request.session['cart_id'] = cart.cart_id

    return cart