from django.contrib import admin

from blogs.models import BlogAuthorModel, BlogCategoryModel, BlogCommentModel, BlogModel, BlogTagModel

admin.site.register(BlogCategoryModel)
admin.site.register(BlogTagModel)
admin.site.register(BlogAuthorModel)
admin.site.register(BlogModel)
admin.site.register(BlogCommentModel)
