from django.db.models import Q
from django.views.generic import ListView, TemplateView, DetailView

from shop.models import *

class ProductTemplateView(ListView):
    template_name = 'shop/products-list.html'
    context_object_name = 'products'
    paginate_by = 3

    def get_queryset(self):
        products = ProductModel.objects.all()
        q = self.request.GET.get('q')
        cat = self.request.GET.get('cat')
        tag = self.request.GET.get('tag')
        color = self.request.GET.get('color')
        size = self.request.GET.get('size')
        sort:str = self.request.GET.get('sort')
        if q:
            products = products.filter(
                Q(title__icontains=q))
        if cat:
            products = products.filter(Q(categories=cat))
        if tag:
            products = products.filter(Q(tags=tag))
        if color:
            products = products.filter(Q(colors=color))
        if size:
            products = products.filter(Q(sizes=size))
        if sort:
            products = products.order_by(sort)
        return products
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sizes"] = ProductSizeModel.objects.all()
        context["colors"] = self.format_colors()
        context["categories"] = ProductCategoryModel.objects.all()
        context["tags"] = ProductTagModel.objects.all()
        context["products_count"] = ProductModel.objects.count()
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
    

class ProductDetailTemplateView(DetailView):
    template_name = 'shop/product-detail.html'
    model = ProductModel
    context_object_name = 'product'
    
