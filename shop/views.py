from django.views.generic import ListView, TemplateView

from shop.models import ProductModel

class ProductTemplateView(ListView):
    template_name = 'shop/products-list.html'
    model = ProductModel
    context_object_name = 'products'

class ProductDetailTemplateView(TemplateView):
    template_name = 'shop/product-detail.html'
