from django.db.models import Q
from django.views.generic import ListView, TemplateView

from shop.models import *

class ProductTemplateView(ListView):
    template_name = 'shop/products-list.html'
    context_object_name = 'products'
    paginate_by = 1

    def get_queryset(self):
        products = ProductModel.objects.all()
        q = self.request.GET.get('q')
        if q:
            products = products.filter(
                Q(title__icontains=q) | Q(description__icontains=q)
            )
        return products
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sizes"] = ProductSizeModel
        context["colors"] = ProductColorModel
        context["categories"] = ProductCategoryModel
        context["tags"] = ProductTagModel
        return context
    

class ProductDetailTemplateView(TemplateView):
    template_name = 'shop/product-detail.html'
