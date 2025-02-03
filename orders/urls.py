from django.urls import path
from orders.views import UserCartListView, add_or_remove_cart, add_or_remove_wishlist, Wishlist_View

app_name = 'orders'

urlpatterns = [
    path('cart/add-or-remove/<int:pk>/', add_or_remove_cart, name='add-or-remove-cart'),
    path('cart/', UserCartListView.as_view(), name="cart"),
    path("wishlist/add-or-remove/<int:pk>/", add_or_remove_wishlist, name="add-or-remove-wishlist"),
    path('all_wishlist/', Wishlist_View.as_view(), name='wishlist')
]
