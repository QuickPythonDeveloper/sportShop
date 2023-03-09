from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from manageProduct.models.defineProduct import DefineProduct

from manageProduct.serializers.product.define import DefineProductSz


class HandleProduct(GenericAPIView):

    def get(self, request, prod_id):

        product = get_object_or_404(DefineProduct, id=prod_id)
        serializer = DefineProductSz(product)
        return Response({'status': 'get product',
                         'product': serializer.data})

    def post(self, request, cat_id):

        sz_data = {}
        sz_data.update(request.data)
        sz_data.update(cat_id=cat_id)
        serializer = DefineProductSz(data=sz_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'status': 'created product',
                         'product': serializer.data})

    def put(self, request, cat_id, prod_id):

        product = get_object_or_404(DefineProduct, id=prod_id)
        sz_data = {}
        sz_data.update(request.data)
        sz_data.update(cat_id=cat_id)
        serializer = DefineProductSz(product, data=sz_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'status': 'updated product',
                         'product': serializer.data})

    def delete(self, request, prod_id):

        product = get_object_or_404(DefineProduct, id=prod_id)
        product.delete()

        return Response({'status': 'deleted product'})
