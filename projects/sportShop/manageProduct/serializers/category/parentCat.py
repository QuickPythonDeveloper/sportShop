from rest_framework import serializers

from ...models.productCategory import ProductCategory


class ParentCatSz(serializers.ModelSerializer):

    parent = serializers.SerializerMethodField()

    class Meta:

        model = ProductCategory
        fields = ['id',
                  'title',
                  'description',
                  'parent']

    def get_parent(self, obj):

        parent = obj.parent
        serializer = ParentCatSz(parent)
        return serializer.data

