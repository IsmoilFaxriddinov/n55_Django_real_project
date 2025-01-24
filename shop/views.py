from django.views.generic import ListView, TemplateView

from shop.models import *

class ProductTemplateView(ListView):
    template_name = 'shop/products-list.html'
    model = ProductModel
    context_object_name = 'products'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sizes"] = ProductSizeModel
        context["colors"] = ProductColorModel
        context["categories"] = ProductCategoryModel
        context["tags"] = ProductTagModel
        return context
    

class ProductDetailTemplateView(TemplateView):
    template_name = 'shop/product-detail.html'
