from django.urls import path
from pages.views import BlogListTemplateView, HomeTemplateView

app_name = 'pages'

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('blogs/', BlogListTemplateView.as_view(), name='blogs')
]
