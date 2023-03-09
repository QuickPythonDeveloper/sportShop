from rest_framework import serializers

from ...models.productCategory import ProductCategory

from .parentCat import ParentCatSz
from .childCat import ChildCatSz
from .allCat import AllProdCatSz


class ProductCatSz(AllProdCatSz):

    parent = serializers.SerializerMethodField()
    childCats = serializers.SerializerMethodField()
    next_id = serializers.SerializerMethodField()
    prev_id = serializers.SerializerMethodField()

    class Meta:

        model = ProductCategory
        fields = ['id',
                  'title',
                  'description',
                  'parent',
                  'childCats',
                  'next_id',
                  'prev_id',
                  'icon',
                  'image']

        read_only_fields = ['id',
                            'parent',
                            'childCats',
                            'next_id',
                            'prev_id']

    def get_parent(self, obj):

        parent = obj.parent
        if parent is None:
            return None

        serializer = ParentCatSz(parent)
        return serializer.data

    def get_childCats(self, obj):

        cats = ProductCategory.objects.filter(parent=obj)
        if not cats.exists():
            return None

        serializer = ChildCatSz(cats, many=True)
        return serializer.data

    def get_next_id(self, obj):

        nxt_objs = ProductCategory.objects.filter(id__gt=obj.id)
        if nxt_objs.exists():
            nxt_obj = nxt_objs.first()
            return nxt_obj.id
        return None

    def get_prev_id(self, obj):

        prev_objs = ProductCategory.objects.filter(id__lt=obj.id)
        if prev_objs.exists():
            prev_obj = prev_objs.last()
            return prev_obj.id
        return None

    def create(self, validated_data):

        cat = ProductCategory.objects.create(**validated_data)
        return cat

    def update(self, instance, validated_data):

        instance.title = validated_data['title']
        instance.description = validated_data['description']
        instance.save()

        return instance
