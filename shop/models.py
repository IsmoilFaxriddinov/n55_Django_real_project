from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class ColorModel(BaseModel):
    heh_code = models.CharField(max_length=125)
    color_name = models.CharField(max_length=125)

    def __str__(self):
        return self.color_name
    
    class Meta:
        verbose_name = 'color'
        verbose_name_plural = 'colors'

class ProductModel(BaseModel):
    image = models.ImageField(upload_to='products/')
    image2 = models.ImageField(upload_to='products/')
    title = models.CharField(max_length=125)
    color = models.ForeignKey(ColorModel, on_delete=models.CASCADE, null=True, blank=True)
    price = models.FloatField()
    description = models.TextField

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class ProductCategoryModel(BaseModel):
    title = models.CharField(max_length=125, verbose_name=('title'))
    parent = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children', verbose_name=('parent'))

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ('blog category')
        verbose_name_plural = ('blog cetegories')

class TagModel(BaseModel):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
    
# class PriceModel(BaseModel):
#     price = models.FloatField()

#     def __str__(self):
#         return self.price
    
#     class Meta:
#         verbose_name = 'price'
#         verbose_name_plural = 'prices'