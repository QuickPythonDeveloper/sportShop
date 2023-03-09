from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from ....models.productAttr import ProductAttr
from ....models.defineProduct import DefineProduct

from ....serializers.product.attr import ProdAttrSz


class HandleProdAttr(GenericAPIView):

    def get(self, request, attr_id):

        attr = get_object_or_404(ProductAttr, id=attr_id)
        sz = ProdAttrSz(attr)
        return Response({'status': 'get product attr',
                         'attr': sz.data})

    def post(self, request, prod_id):

        product = get_object_or_404(DefineProduct, id=prod_id)
        attrs = ProductAttr.objects.filter(product=product)
        if attrs.count() == 3:
            return Response({'status': 'max number of attrs'})

        sz_data = {}
        sz_data.update(request.data)
        sz_data.update(product_id=prod_id)
        sz = ProdAttrSz(data=sz_data)
        sz.is_valid(raise_exception=True)
        sz.save()

        return Response({'status': 'added attr to product',
                         'attr': sz.data})

    def put(self, request, attr_id):

        attr = get_object_or_404(ProductAttr, id=attr_id)
        sz_data = {}
        sz_data.update(request.data)
        sz_data.update(product_id=attr.product.id)
        sz = ProdAttrSz(attr, data=sz_data)
        sz.is_valid(raise_exception=True)
        sz.save()

        return Response({'status': 'updated product attr',
                         'attr': sz.data})

    def delete(self, request, attr_id):

        attr = get_object_or_404(ProductAttr, id=attr_id)
        attr.delete()

        return Response({'status': 'deleted product attr'})
