from rest_framework import serializers
from django.shortcuts import get_object_or_404

from manageProduct.models.defineProduct import DefineProduct
from manageProduct.models.productCategory import ProductCategory
from manageProduct.models.productAttr import ProductAttr
from manageProduct.models.productProp import ProductProp
from manageProduct.models.galleryImage import GalleryImage

from manageProduct.serializers.category.category import ProductCatSz
from manageProduct.serializers.product.attr import ProdAttrSz
from manageProduct.serializers.product.prop import ProdPropSz
from manageProduct.serializers.product.gImage import ProdGalImageSz


class DefineProductSz(serializers.ModelSerializer):

    category = serializers.SerializerMethodField()
    cat_id = serializers.IntegerField()
    attrs = serializers.SerializerMethodField()
    next_id = serializers.SerializerMethodField()
    prev_id = serializers.SerializerMethodField()
    props = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()

    class Meta:

        model = DefineProduct
        fields = ['id',
                  'cat_id',
                  'category',
                  'title',
                  'note',
                  'attrs',
                  'next_id',
                  'prev_id',
                  'props',
                  'images']

        read_only_fields = ['id',
                            'category',
                            'next_id',
                            'prev_id',
                            'props'
                            ]
        write_only_fields = ['cat_id']

    def get_images(self, obj):

        imgs = GalleryImage.objects.filter(product=obj)
        if not imgs.exists():
            return None

        sz = ProdGalImageSz(imgs, many=True)
        return sz.data

    def get_category(self, obj):

        cat = obj.cat
        serializer = ProductCatSz(cat)
        return serializer.data

    def get_attrs(self, obj):

        attrs = ProductAttr.objects.filter(product=obj)
        sz = ProdAttrSz(attrs, many=True)
        return sz.data

    def get_next_id(self, obj):

        nxt_objs = DefineProduct.objects.filter(id__gt=obj.id)
        if nxt_objs.exists():
            nxt_obj = nxt_objs.first()
            return nxt_obj.id
        return None

    def get_prev_id(self, obj):

        prev_objs = DefineProduct.objects.filter(id__lt=obj.id)
        if prev_objs.exists():
            prev_obj = prev_objs.last()
            return prev_obj.id
        return None

    def get_props(self, obj):

        props = ProductProp.objects.filter(product=obj)
        sz = ProdPropSz(props, many=True)
        return sz.data

    def create(self, validated_data):

        category = get_object_or_404(ProductCategory, id=validated_data['cat_id'])
        product = DefineProduct.objects.create(cat=category,
                                               title=validated_data['title'],
                                               note=validated_data['note'])
        return product

    def update(self, instance, validated_data):

        category = get_object_or_404(ProductCategory, id=validated_data['cat_id'])
        instance.cat = category
        instance.title = validated_data['title']
        instance.note = validated_data['note']
        instance.save()

        return instance
