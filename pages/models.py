from django.db import models

class ProductModel(models.Model):
    image = models.ImageField(upload_to='products/')
    title = models.CharField(max_length=125)
    price = models.FloatField()

    def __str__(self):
        return self.title

class CategoryModel(models.Model):
    ...

class ColorModel(models.Model):
    heh_code = models.IntegerField()
    color_name = models.CharField(max_length=125)

    def __str__(self):
        return self.color_name

class TagModel(models.Model):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name