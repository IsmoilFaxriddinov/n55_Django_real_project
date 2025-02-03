from django.contrib import admin
from .models import OrderModel, OrderItem

@admin.register(OrderModel)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'total_amound', 'total_product', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'total_amound')
    ordering = ('-created_at',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'product_name', 'product_price', 'quantity', 'created_at')
    list_filter = ('order',)
    search_fields = ('product_name', 'order__user__username')
    ordering = ('-created_at',)