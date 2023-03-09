from rest_framework import serializers

from ...models.productCategory import ProductCategory


class ChildCatSz(serializers.ModelSerializer):

    childCats = serializers.SerializerMethodField()

    class Meta:

        model = ProductCategory
        fields = ['id',
                  'title',
                  'description',
                  'childCats']

    def get_childCats(self, obj):

        cats = ProductCategory.objects.filter(parent=obj)
        serializer = ChildCatSz(cats, many=True)
        return serializer.data
