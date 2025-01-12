from django.views.generic import TemplateView

class HomeTemplateView(TemplateView):
    template_name = 'pages/home.html'

class BlogListTemplateView(TemplateView):
    template_name = 'blogs/blog-list.html'

class ProductTemplateView(TemplateView):
    template_name = 'shop/products-list.html'