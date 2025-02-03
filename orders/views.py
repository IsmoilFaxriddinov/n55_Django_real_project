from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, FormView
from django.urls import reverse_lazy

from shop.models import ProductModel


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
    template_name = 'shop/product-wishlist.html'

class UserCartListView(ListView):
    template_name = 'shop/product-cart.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        cart = self.request.session.get('cart', [])
        products = ProductModel.objects.filter(id__in=cart)

        return products

class CheckoutCreateView(FormView):
    template_name = 'shop/product-checkout.html'
    form_class = ...
    success_url = reverse_lazy("users:account")

    
    