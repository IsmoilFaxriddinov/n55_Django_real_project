from modeltranslation.translator import register, TranslationOptions

from . import models

@register(models.BlogCategoryModel)
class BlogCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(models.BlogTagModel)
class BlogTagTranslationOption(TranslationOptions):
    fields = ('title',)

@register(models.BlogAuthorModel)
class BlogAuthorTranslationOption(TranslationOptions):
    fields = ('first_name', 'last_name')

@register(models.BlogModel)
class BlogModelTranslationOption(TranslationOptions):
    fields = ('title', 'description')