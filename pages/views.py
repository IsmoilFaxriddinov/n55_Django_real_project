from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import login_required

from blogs.models import BlogModel

class HomeTemplateView(TemplateView):
    template_name = 'pages/home.html'

class BlogListTemplateView(ListView):
    template_name = 'blogs/blog-list.html'
    model = BlogModel
    context_object_name = 'blogs'
    