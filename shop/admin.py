from django.contrib import admin
from shop.models import ColorModel, ProductCategoryModel, ProductCommentModel, ProductImageModel, ProductModel, ProductSizeModel, TagModel

admin.site.register(ColorModel)
admin.site.register(ProductCategoryModel)
admin.site.register(TagModel)
admin.site.register(ProductSizeModel)
admin.site.register(ProductModel)
admin.site.register(ProductImageModel)
admin.site.register(ProductCommentModel)
