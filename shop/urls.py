from django.urls import path
from shop.views import ProductTemplateView

urlpatterns = [
    path('products/', ProductTemplateView.as_view(), name='products'),
]
