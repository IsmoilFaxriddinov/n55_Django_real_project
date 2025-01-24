from django.contrib import admin
from shop.models import ProductColorModel, ProductCategoryModel, ProductCommentModel, ProductImageModel, ProductModel, ProductSizeModel, ProductTagModel

admin.site.register(ProductColorModel)
admin.site.register(ProductCategoryModel)
admin.site.register(ProductTagModel)
admin.site.register(ProductSizeModel)
admin.site.register(ProductModel)
admin.site.register(ProductImageModel)
admin.site.register(ProductCommentModel)
