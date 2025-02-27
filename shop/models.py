from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from app_common.models import BaseModel

userModel = get_user_model()

class ProductColorModel(BaseModel):
    code = models.CharField(max_length=125, verbose_name=_('code'))
    title = models.CharField(max_length=125, verbose_name=_('title'))

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _('color')
        verbose_name_plural = _('colors')


class ProductCategoryModel(BaseModel):
    title = models.CharField(max_length=125, verbose_name=_('title'))
    parent = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children', verbose_name=_('parent'))

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _('blog category')
        verbose_name_plural = _('blog cetegories')

class ProductTagModel(BaseModel):
    name = models.CharField(max_length=125, verbose_name=_('name'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')
    
class ProductSizeModel(BaseModel):
    name = models.CharField(max_length=125, verbose_name=_('name'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('size')
        verbose_name_plural = _('sizes')

class ProductModel(BaseModel):
    image1 = models.ImageField(upload_to='products/')
    image2 = models.ImageField(upload_to='products/')
    discount = models.SmallIntegerField(null=True, blank=True)
    title = models.CharField(max_length=125, verbose_name=_('title'))
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(verbose_name=_('description'))
    sku = models.CharField(max_length=125)
    in_stuck = models.BooleanField(default=True)

    color = models.ManyToManyField(ProductColorModel, related_name='colors', verbose_name=_('color'))
    tags = models.ManyToManyField(ProductTagModel, related_name='tags', verbose_name=_('tags'))
    categories = models.ManyToManyField(ProductCategoryModel, related_name='categories', verbose_name=_('categories'))
    sizes = models.ManyToManyField(ProductSizeModel, related_name='sizes', verbose_name=_('size'))

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

class ProductImageModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/images/')

class ProductCommentModel(BaseModel):
    comment = models.CharField(max_length=125, verbose_name=_('comment'))
    user = models.ForeignKey(userModel, on_delete=models.CASCADE, related_name='user')
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    