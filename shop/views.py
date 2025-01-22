from django.views.generic import ListView, TemplateView

from shop.models import ProductModel

class ProductTemplateView(ListView):
    template_name = 'shop/products-list.html'
    model = ProductModel

class ProductDetailTemplateView(TemplateView):
    template_name = 'shop/products-list.html'
