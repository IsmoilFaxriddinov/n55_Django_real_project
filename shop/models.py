from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class ProductModel(BaseModel):
    image = models.ImageField(upload_to='products/')
    title = models.CharField(max_length=125)
    price = models.FloatField()

    def __str__(self):
        return self.title

class ProductCategoryModel(BaseModel):
    title = models.CharField(max_length=125, verbose_name=('title'))
    parent = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children', verbose_name=('parent'))

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ('blog category')
        verbose_name_plural = ('blog cetegories')

class ColorModel(BaseModel):
    heh_code = models.IntegerField()
    color_name = models.CharField(max_length=125)

    def __str__(self):
        return self.color_name

class TagModel(BaseModel):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name