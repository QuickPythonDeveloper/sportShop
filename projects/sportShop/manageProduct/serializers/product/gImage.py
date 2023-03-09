from rest_framework import serializers

from django.shortcuts import get_object_or_404

from manageProduct.models.galleryImage import GalleryImage
from manageProduct.models.defineProduct import DefineProduct


class ProdGalImageSz(serializers.ModelSerializer):

    product_id = serializers.IntegerField()
    #cat_id = serializers.IntegerField()
    next_id = serializers.SerializerMethodField()
    prev_id = serializers.SerializerMethodField()

    class Meta:

        model = GalleryImage
        fields = ['id',
                  'product_id',
                  'image',
                  'is_icon',
                  'thumbnail',
                  'height',
                  'width',
                  'orig_size',
                  'thumb_size',
                  'format',
                  'next_id',
                  'prev_id']

        read_only_fields = ['id',
                            'width',
                            'height',
                            'size',
                            'format',
                            'next_id',
                            'prev_id']

    def get_next_id(self, obj):

        nxt_objs = GalleryImage.objects.filter(id__gt=obj.id)
        if nxt_objs.exists():
            nxt_obj = nxt_objs.first()
            return nxt_obj.id
        return None

    def get_prev_id(self, obj):

        prev_objs = GalleryImage.objects.filter(id__lt=obj.id)
        if prev_objs.exists():
            prev_obj = prev_objs.last()
            return prev_obj.id
        return None

    def create(self, validated_data):

        product = get_object_or_404(DefineProduct, id=validated_data['product_id'])
        img = GalleryImage.objects.create(product=product,
                                          image=validated_data['image'])

        img.height = img.image.height
        img.width = img.image.width
        img.orig_size = img.image.size
        img.format = img.image.url.split(".")[1]
        img.save()

        return img
