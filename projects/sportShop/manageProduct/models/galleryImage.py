from django.db import models

from .defineProduct import DefineProduct
from .productCategory import ProductCategory


class GalleryImage(models.Model):
    product = models.ForeignKey(DefineProduct,
                                on_delete=models.CASCADE,
                                null=True)
    cat = models.ForeignKey(ProductCategory,
                            on_delete=models.CASCADE,
                            null=True)
    image = models.ImageField(upload_to='images')
    is_icon = models.BooleanField(default=False)
    thumbnail = models.ImageField(upload_to='thumbnails',
                                  null=True,
                                  blank=True)
    height = models.PositiveIntegerField(null=True,
                                         blank=True)
    width = models.PositiveIntegerField(null=True,
                                        blank=True)
    orig_size = models.PositiveIntegerField(null=True,
                                            blank=True)
    thumb_size = models.PositiveIntegerField(null=True,
                                             blank=True)
    format = models.CharField(max_length=30,
                              null=True,
                              blank=True)
