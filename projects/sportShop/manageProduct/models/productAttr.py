from django.db import models

from .defineProduct import DefineProduct


class ProductAttr(models.Model):
    product = models.ForeignKey(DefineProduct,
                                on_delete=models.CASCADE)
    key = models.CharField(max_length=30)
    value = models.CharField(max_length=200)
    note = models.TextField(null=True,
                            blank=True)

    class Meta:
        unique_together = [('product', 'key')]
