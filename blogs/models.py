from django.db import models
from django.contrib.auth import get_user_model
from app_common.models import BaseModel
from django.utils.translation import gettext_lazy as _

UserModel = get_user_model()

class BlogCategoryModel(BaseModel):
    title = models.CharField(max_length=125, verbose_name=_('title'))
    parent = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children', verbose_name=_('parent'))

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _('blog category')
        verbose_name_plural = _('blog cetegories')

class BlogTagModel(BaseModel):
    title = models.CharField(max_length=125, verbose_name=_('title'))
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _('blog tag')
        verbose_name_plural = _('blog tags')

class BlogAuthorModel(BaseModel):
    first_name = models.CharField(max_length=125, verbose_name=_('first_name'))
    last_name = models.CharField(max_length=125, verbose_name=_('last_name'))
    avatar = models.ImageField(upload_to='blogs/avatars/', verbose_name=_('avatar'))
    title = models.CharField(max_length=125, verbose_name=_('title'))
    parent = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, verbose_name=_('parent'))

    def __str__(self):
        return self.first_name
    
    class Meta:
        verbose_name = _('Blog author')
        verbose_name_plural = _('Blog authors')
    
class BlogModel(BaseModel):
    image = models.ImageField(upload_to='blogs', verbose_name=_('image'))
    title = models.CharField(max_length=125, verbose_name=_('title'))
    description = models.TextField(verbose_name=_('description'))

    author = models.ManyToManyField(BlogAuthorModel, related_name=_('blogs'))
    categories = models.ManyToManyField(BlogCategoryModel, related_name=_('blog'))
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _('Blog')
        verbose_name_plural = _('Blogs')

class BlogCommentModel(BaseModel):
    comment = models.CharField(max_length=125, verbose_name=_('comment'))
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='blog_comments', verbose_name=_('user'))

    author = models.ManyToManyField(BlogAuthorModel, related_name=_('blog_author'))
    categories = models.ManyToManyField(BlogCategoryModel, related_name=_('blogs'))
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = _('Blog comment')
        verbose_name_plural = _('Blog comments')