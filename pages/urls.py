from django.urls import path
from pages.views import BlogListTemplateView, HomeTemplateView, ProductTemplateView

app_name = 'pages'

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('blogs/', BlogListTemplateView.as_view(), name='blogs'),
    path('products/', ProductTemplateView.as_view(), name='products'),
]
