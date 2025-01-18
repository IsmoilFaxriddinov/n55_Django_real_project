from django.contrib import admin
from shop.models import ProductModel, ProductCategoryModel, TagModel, ColorModel

admin.site.register(ProductModel)
admin.site.register(ProductCategoryModel)
admin.site.register(TagModel)
admin.site.register(ColorModel)