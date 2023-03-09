from django.db import models


class ProductCategory(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,
                                   blank=True)
    parent = models.ForeignKey('self',
                               on_delete=models.SET_NULL,
                               related_name='child',
                               null=True,
                               blank=True)
