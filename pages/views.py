from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import login_required

from blogs.models import BlogCategoryModel, BlogModel, BlogTagModel

class HomeTemplateView(TemplateView):
    template_name = 'pages/home.html'

class BlogListTemplateView(ListView):
    template_name = 'blogs/blog-list.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        
        tag = self.request.GET.get('tag')
        blogs = BlogModel.objects.all()
        category = self.request.GET.get('category')
        if tag:
            blogs = blogs.filter(tags=tag)
        elif category:
            blogs = blogs.filter(categories=category)
        return blogs
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = BlogCategoryModel.objects.all()
        context["recent_blogs"] = BlogModel.objects.order_by('-created_at')[:2]
        context["tags"] = BlogTagModel.objects.all()
        return context
    