from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import TemplateView, ListView, FormView
from django.urls import reverse_lazy
from django.db.models.aggregates import Sum
from django.contrib.auth.mixins import LoginRequiredMixin

from orders.forms import CheckoutForm
from orders.models import OrderItem, OrderModel
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

class CheckoutCreateView(LoginRequiredMixin, FormView):
    template_name = 'shop/product-checkout.html'
    form_class = CheckoutForm
    success_url = reverse_lazy("users:account")

    def calculate_total_price(self, products):
        total = 0
        for product in products:
            total += product.price
        return total

    def form_valid(self, form):
        user = self.request.user
        cart = self.request.session.get('cart', [])
        products = ProductModel.objects.filter(id__in=cart)
        if len(products) == 0:
            messages.info(self.request, "Add some products")
            return redirect(reverse_lazy("shop:list"))
        else:
            order = OrderModel.objects.create(user=user, status=False, total_amound=self.calculate_total_price(products), total_product=len(products))
            for product in products:
                product_info = ProductModel.objects.get(id=product.id)
                OrderItem.objects.create(order=order, quantity=1, product=product, product_name=product_info.title, product_price=product_info.price)
            return redirect(reverse_lazy('users:account'))
    
    def form_invalid(self, form):
        return super().form_invalid(form)
    