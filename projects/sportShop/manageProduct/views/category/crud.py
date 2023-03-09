from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from ...serializers.category.category import ProductCatSz

from ...models.productCategory import ProductCategory


class HandleProductCat(GenericAPIView):

    def get(self, request, cat_id):

        cat = get_object_or_404(ProductCategory, id=cat_id)
        serializer = ProductCatSz(cat)
        return Response({'status': 'get product category',
                         'cat': serializer.data})

    def post(self, request):

        serializer = ProductCatSz(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'status': 'created product category',
                         'cat': serializer.data})

    def put(self, request, cat_id):

        cat = get_object_or_404(ProductCategory, id=cat_id)
        serializer = ProductCatSz(cat, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': 'updated product category',
                         'cat': serializer.data})

    def delete(self, request, cat_id):

        cat = get_object_or_404(ProductCategory, id=cat_id)
        cat.delete()
        return Response({'status': 'deleted product category'})
