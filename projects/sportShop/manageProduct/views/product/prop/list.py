from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from manageProduct.models.productProp import ProductProp
from manageProduct.models.defineProduct import DefineProduct

from manageProduct.serializers.product.prop import ProdPropSz


class ProdPropList(GenericAPIView):

    def get(self, request, prod_id):

        prod = get_object_or_404(DefineProduct, id=prod_id)
        props = ProductProp.objects.filter(product=prod)
        sz = ProdPropSz(props, many=True)

        return Response({'status': 'get props of a product',
                         'props': sz.data})
