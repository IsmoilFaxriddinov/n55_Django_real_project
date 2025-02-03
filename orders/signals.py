from django.dispatch import receiver
from django.db.models.signals import pre_save

from shop.models import ProductModel

@receiver(pre_save, sender=ProductModel)
def update_product_price(sender, instance, **kwargs):
    if instance.discount:
        instance.discount_price = instance.price - (instance.price * 100 / instance.discount)
    else:
        instance.discount_price = instance.price
