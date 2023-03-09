from rest_framework import serializers

from django.shortcuts import get_object_or_404

from manageProduct.models.productProp import ProductProp
from manageProduct.models.defineProduct import DefineProduct


class ProdPropSz(serializers.ModelSerializer):

    product_id = serializers.IntegerField()
    next_id = serializers.SerializerMethodField()
    prev_id = serializers.SerializerMethodField()
    cat_id = serializers.SerializerMethodField()
    prod_id = serializers.SerializerMethodField()

    class Meta:

        model = ProductProp
        fields = ['id',
                  'product_id',
                  'weight',
                  'size',
                  'color',
                  'price',
                  'stock_count',
                  'pre_order_count',
                  'next_id',
                  'prev_id',
                  'cat_id',
                  'prod_id']

        read_only_fields = ['pre_order_count',
                            'next_id',
                            'prev_id',
                            'prod_id',
                            'cat_id']

    def get_next_id(self, obj):

        nxt_objs = ProductProp.objects.filter(id__gt=obj.id)
        if nxt_objs.exists():
            nxt_obj = nxt_objs.first()
            return nxt_obj.id
        return None

    def get_prev_id(self, obj):

        prev_objs = ProductProp.objects.filter(id__lt=obj.id)
        if prev_objs.exists():
            prev_obj = prev_objs.last()
            return prev_obj.id
        return None

    def get_cat_id(self, obj):

        prod = obj.product
        cat = prod.cat
        return cat.id

    def get_prod_id(self, obj):

        prod = obj.product
        return prod.id

    def create(self, validated_data):

        prod = get_object_or_404(DefineProduct, id=validated_data['product_id'])
        prop = ProductProp.objects.create(product=prod,
                                          weight=validated_data['weight'],
                                          size=validated_data['size'],
                                          color=validated_data['color'],
                                          price=validated_data['price'],
                                          stock_count=validated_data['stock_count'])
        return prop

    def update(self, instance, validated_data):

        instance.weight = validated_data['weight']
        instance.size = validated_data['size']
        instance.color = validated_data['color']
        instance.price = validated_data['price']
        instance.stock_count = validated_data['stock_count']

        instance.save()
        return instance
