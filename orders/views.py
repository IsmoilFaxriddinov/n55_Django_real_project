from django.shortcuts import redirect


def add_or_remove_cart(request, pk):
    cart: list = request.session.get('cart', [])
    if pk in cart:
        cart.remove(pk)
    else:
        cart.append(pk)

    request.session['cart'] = cart
    return redirect()

def add_or_remove_wishlist(request, pk):
    ...