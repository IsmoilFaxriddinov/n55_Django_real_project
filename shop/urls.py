from django.urls import path
from shop.views import ProductDetailTemplateView, ProductTemplateView

app_name="shop"

urlpatterns = [
    path('products/', ProductTemplateView.as_view(), name='list'),
    path('product/<detail>', ProductDetailTemplateView.as_view(), name='detail'),
]
