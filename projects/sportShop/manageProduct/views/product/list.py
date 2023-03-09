from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from manageProduct.models.productCategory import ProductCategory
from manageProduct.models.defineProduct import DefineProduct

from manageProduct.serializers.product.define import DefineProductSz


class ProdList(GenericAPIView):

    def get(self, request, cat_id):

        cat = get_object_or_404(ProductCategory, id=cat_id)
        prods = DefineProduct.objects.filter(cat=cat)
        serializer = DefineProductSz(prods, many=True)

        return Response({'status': 'get products list in a category',
                         'products': serializer.data})
