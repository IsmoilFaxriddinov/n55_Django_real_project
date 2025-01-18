from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

class HomeTemplateView(TemplateView):
    template_name = 'pages/home.html'

class BlogListTemplateView(TemplateView):
    template_name = 'blogs/blog-list.html'