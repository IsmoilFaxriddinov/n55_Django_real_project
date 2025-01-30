from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.urls import reverse_lazy


def add_or_remove_cart(request, pk):
    cart: list = request.session.get('cart', [])
    if pk in cart:
        cart.remove(pk)
    else:
        cart.append(pk)

    request.session['cart'] = cart
    next = request.GET.get('next', reverse_lazy('products:list'))
    return redirect(next)

def add_or_remove_wishlist(request, pk):
    wishlist: list = request.session.get('wishlist', [])
    if pk in wishlist:
        wishlist.remove(pk)
    else:
        wishlist.append(pk)

    request.session['wishlist'] = wishlist
    next = request.GET.get('next', reverse_lazy('products:list'))
    return redirect(next)


class Wishlist_View(TemplateView):
    template_name = 'shop/product-cart.html'