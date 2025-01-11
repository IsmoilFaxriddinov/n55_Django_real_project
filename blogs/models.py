from django.db import models

class CategoryModel(models.Model):
    category_name = models.CharField(max_length=125)

    craeted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

class RecentPointModel(models.Model):
    name = models.CharField(max_length=125)
    short_description = models.CharField(max_length=80)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{ self.name } | {self.short_description}"
    
    class Meta:
        verbose_name = 'Recent Posts'
    
class 