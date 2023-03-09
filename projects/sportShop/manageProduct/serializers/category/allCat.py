from rest_framework import serializers

from ...models.productCategory import ProductCategory
from ...models.galleryImage import GalleryImage

from ..product.gImage import ProdGalImageSz


class AllProdCatSz(serializers.ModelSerializer):

    icon = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    class Meta:

        model = ProductCategory
        fields = ['id',
                  'title',
                  'description',
                  'image',
                  'icon']

    def get_icon(self, obj):

        icons = GalleryImage.objects.filter(cat=obj,
                                            is_icon=True)
        if not icons.exists():
            return None

        icon = icons.first()
        sz = ProdGalImageSz(icon)
        return sz.data

    def get_image(self, obj):

        imgs = GalleryImage.objects.filter(cat=obj,
                                           is_icon=False)
        if not imgs.exists():
            return None

        img = imgs.first()
        sz = ProdGalImageSz(img)
        return sz.data
