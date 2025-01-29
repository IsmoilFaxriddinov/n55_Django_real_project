from django import template

from shop.models import ProductModel

register = template.Library()

@register.filter
def in_cart(request, pk):
    return pk in request.session.get('cart', [])

@register.filter
def get_user_cart(request):
    cart = request.session.get('cart', [])
    products = []
    for pk in cart:
        product = ProductModel.objects.filter(pk=pk)
        products.append(product)
    return products        
