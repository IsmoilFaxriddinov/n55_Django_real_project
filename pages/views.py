from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

@login_required(login_url='users/login')
class HomeTemplateView(TemplateView):
    template_name = 'pages/home.html'

class BlogListTemplateView(TemplateView):
    template_name = 'blogs/blog-list.html'

class ProductTemplateView(TemplateView):
    template_name = 'shop/products-list.html'