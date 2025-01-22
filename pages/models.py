from django.db import models
from django.utils.translation import gettext_lazy as _

from app_common.models import BaseModel

class ContactModel(BaseModel):
    name = models.CharField(max_length=125, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    subject = models.CharField(max_length=125, verbose_name=_('subject'))
    message = models.TextField(verbose_name=_('message'))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')
