from django.urls import path
from shop.views import ProductTemplateView

app_name="shop"

urlpatterns = [
    path('products/', ProductTemplateView.as_view(), name='products'),
]
