from django.db import models
from django.contrib.auth import get_user_model
from app_common.models import BaseModel

UserModel = get_user_model()

class OrderModel(BaseModel):
    user = models.ForeignKey(UserModel, on_delete=models.PROTECT, related_name='orders')
    status = models.BooleanField(default=False)
    total_amound = models.DecimalField(max_digits=10, decimal_places=2)
    total_product = models.PositiveSmallIntegerField()

