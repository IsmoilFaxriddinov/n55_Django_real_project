from django.db import models
from django.contrib.auth import get_user_model
from app_common.models import BaseModel
from shop.models import ProductModel

UserModel = get_user_model()

class OrderModel(BaseModel):
    user = models.ForeignKey(UserModel, on_delete=models.PROTECT, related_name='orders')
    status = models.BooleanField(default=False)
    total_amound = models.DecimalField(max_digits=10, decimal_places=2)
    total_product = models.PositiveSmallIntegerField()


class OrderItem(BaseModel):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE, related_name=('items'))
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name=('ordered'))
    product_name = models.CharField(max_length=125)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveSmallIntegerField()

    