from django.db import models
from django.contrib.auth import get_user_model
from app_common.models import BaseModel
from django.utils.translation import gettext_lazy as _

UserModel = get_user_model()

class BlogCategoryModel(BaseModel):
    title = models.CharField(max_length=125)
    parent = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'blog category'
        verbose_name_plural = 'blog cetegories'

class BlogTagModel(BaseModel):
    title = models.CharField(max_length=125)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'blog tag'
        verbose_name_plural = 'blog tags'

class BlogAuthorModel(BaseModel):
    first_name = models.CharField(max_length=125)
    last_name = models.CharField(max_length=125)
    avatar = models.ImageField(upload_to='blogs/avatars/')
    title = models.CharField(max_length=125)
    parent = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.first_name
    
    class Meta:
        verbose_name = 'Blog author'
        verbose_name_plural = 'Blog authors'
    
class BlogModel(BaseModel):
    image = models.ImageField(upload_to='blogs')
    title = models.CharField(max_length=125)
    description = models.TextField()

    author = models.ManyToManyField(BlogAuthorModel, related_name='blogs')
    categories = models.ManyToManyField(BlogCategoryModel, related_name='blog')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

class BlogCommentModel(BaseModel):
    comment = models.CharField(max_length=125)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='blog_comments')

    author = models.ManyToManyField(BlogAuthorModel, related_name='blog_author')
    categories = models.ManyToManyField(BlogCategoryModel, related_name='blogs')
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'Blog comment'
        verbose_name_plural = 'Blog comments'