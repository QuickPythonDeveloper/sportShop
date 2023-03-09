from django.db import models

from .productCategory import ProductCategory


class DefineProduct(models.Model):
    cat = models.ForeignKey(ProductCategory,
                            on_delete=models.CASCADE,
                            related_name='product')
    title = models.CharField(max_length=200)
    note = models.TextField(null=True,
                            blank=True)
    insta_perm = models.BooleanField(default=False)
