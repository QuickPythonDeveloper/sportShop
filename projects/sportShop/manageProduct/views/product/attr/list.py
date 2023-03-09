from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from ....models.defineProduct import DefineProduct
from ....models.productAttr import ProductAttr

from ....serializers.product.attr import ProdAttrSz


class ProdAttrList(GenericAPIView):

    def get(self, request, prod_id):

        product = get_object_or_404(DefineProduct, id=prod_id)
        attrs = ProductAttr.objects.filter(product=product)
        sz = ProdAttrSz(attrs, many=True)

        return Response({'status': 'get attrs of a product',
                         'attrs': sz.data})
