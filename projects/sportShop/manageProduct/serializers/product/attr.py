from rest_framework import serializers

from ...models.productAttr import ProductAttr
from ...models.defineProduct import DefineProduct

from django.shortcuts import get_object_or_404
from django.db import IntegrityError


class ProdAttrSz(serializers.ModelSerializer):

    product_id = serializers.IntegerField()
    next_id = serializers.SerializerMethodField()
    prev_id = serializers.SerializerMethodField()
    cat_id = serializers.SerializerMethodField()

    class Meta:

        model = ProductAttr
        fields = ['id',
                  'product_id',
                  'key',
                  'value',
                  'note',
                  'next_id',
                  'prev_id',
                  'cat_id']

        read_only_fields = ['id',
                            'next_id',
                            'prev_id',
                            'cat_id']
        write_only_fields = ['product_id']

    def get_next_id(self, obj):

        nxt_objs = ProductAttr.objects.filter(id__gt=obj.id)
        if nxt_objs.exists():
            nxt_obj = nxt_objs.first()
            return nxt_obj.id
        return None

    def get_prev_id(self, obj):

        prev_objs = ProductAttr.objects.filter(id__lt=obj.id)
        if prev_objs.exists():
            prev_obj = prev_objs.last()
            return prev_obj.id
        return None

    def get_cat_id(self, obj):

        prod = obj.product
        cat_id = prod.cat.id
        return int(cat_id)

    def create(self, validated_data):

        product = get_object_or_404(DefineProduct, id=validated_data['product_id'])

        try:
            attr = ProductAttr.objects.create(product=product,
                                              key=validated_data['key'],
                                              value=validated_data['value'],
                                              note=validated_data['note'])

            return attr
        except IntegrityError:
            raise serializers.ValidationError({"error": "the key for this prop already exists"})

    def update(self, instance, validated_data):

        instance.key = validated_data['key']
        instance.value = validated_data['value']
        instance.note = validated_data['note']
        instance.save()

        return instance
