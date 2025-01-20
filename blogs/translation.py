from modeltranslation.translator import register, TranslationOptions
from . import models

@register(models.BlogCategoryModel)
class BlogCategoryTranslationOption(TranslationOptions):
    fields = ('title', "text")
