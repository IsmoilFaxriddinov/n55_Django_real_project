from django.contrib import admin
from shop.models import ProductColorModel, ProductCategoryModel, ProductCommentModel, ProductImageModel, ProductModel, ProductSizeModel, ProductTagModel

admin.site.register(ProductColorModel)
admin.site.register(ProductCategoryModel)
admin.site.register(ProductTagModel)
admin.site.register(ProductSizeModel)
admin.site.register(ProductImageModel)
admin.site.register(ProductCommentModel)
@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'in_stuck')
    list_filter = ('in_stuck', 'categories', 'tags')
    search_fields = ('title', 'sku')
    filter_horizontal = ('color', 'tags', 'categories', 'sizes')
    readonly_fields = ['discount_price']