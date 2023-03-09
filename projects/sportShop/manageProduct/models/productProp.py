from django.db import models

from .defineProduct import DefineProduct


class ProductProp(models.Model):
    product = models.ForeignKey(DefineProduct,
                                on_delete=models.CASCADE,
                                related_name='props')
    weight = models.CharField(max_length=20,
                              null=True,
                              blank=True)
    size = models.CharField(max_length=20,
                            null=True,
                            blank=True)
    color = models.CharField(max_length=30,
                             null=True,
                             blank=True)
    price = models.DecimalField(decimal_places=2,
                                max_digits=20)
    stock_count = models.PositiveIntegerField(default=0)
    pre_order_count = models.PositiveIntegerField(default=0)
    insta_posted = models.BooleanField(default=False)
