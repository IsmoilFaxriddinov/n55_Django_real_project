from django import template

register = template.Library()

@register.simple_tag
def get_lang_url(request, lang):
    url = request.path.split('/')
    url[1] = lang
    return '/'.join(url)

@register.simple_tag
def get_lang_flag(lang):
    if lang == 'uz':
        return 'uz'
    elif lang == 'en':
        return 'en'
    else:
        return 'ru'