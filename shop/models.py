from django.db import models
from django.utils.translation import gettext_lazy as _

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class ColorModel(BaseModel):
    code = models.CharField(max_length=125, verbose_name=_('code'))
    title = models.CharField(max_length=125, verbose_name=_('title'))

    def __str__(self):
        return self.color_name
    
    class Meta:
        verbose_name = _('color')
        verbose_name_plural = _('colors')

class ProductModel(BaseModel):
    image1 = models.ImageField(upload_to='products/')
    image2 = models.ImageField(upload_to='products/')
    title = models.CharField(max_length=125, verbose_name=_('title'))
    color = models.ForeignKey(ColorModel, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('color'))
    price = models.FloatField()
    description = models.TextField(verbose_name=_('description'))

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

class ProductCategoryModel(BaseModel):
    title = models.CharField(max_length=125, verbose_name=_('title'))
    parent = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children', verbose_name=_('parent'))

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _('blog category')
        verbose_name_plural = _('blog cetegories')

class TagModel(BaseModel):
    name = models.CharField(max_length=125, verbose_name=_('name'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')
    
# class PriceModel(BaseModel):
#     price = models.FloatField()

#     def __str__(self):
#         return self.price
    
#     class Meta:
#         verbose_name = 'price'
#         verbose_name_plural = 'prices'