from django.urls import path
from shop.views import ProductDetailTemplateView, ProductTemplateView

app_name="shop"

urlpatterns = [
    path('', ProductTemplateView.as_view(), name='list'),
    path('<int:pk>/', ProductDetailTemplateView.as_view(), name='detail'),
]
