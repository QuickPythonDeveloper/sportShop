from django.db import models

from userAccount.models import CustomerUser
from .productProp import ProductProp


class ProdPreOrder(models.Model):
    user = models.ManyToManyField(CustomerUser)
    prop = models.ForeignKey(ProductProp,
                             on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
