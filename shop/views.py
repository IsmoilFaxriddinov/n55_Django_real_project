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
        context["sizes"] = ProductSizeModel.objects.all()
        context["colors"] = self.format_colors()
        context["categories"] = ProductCategoryModel.objects.all()
        context["tags"] = ProductTagModel.objects.all()
        return context
    
    @staticmethod
    def format_colors():
        colors = ProductColorModel.objects.all()
        result = []
        temp_list = []
        for color in colors:
            temp_list.append(color)
            if len(temp_list) == 2:
                result.append(temp_list)
                temp_list = []
        if len(temp_list) == 1:
            result.append(temp_list)
        return result
    

class ProductDetailTemplateView(TemplateView):
    template_name = 'shop/product-detail.html'
