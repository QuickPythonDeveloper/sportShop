from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from ....models.productProp import ProductProp

from ....serializers.product.prop import ProdPropSz


class HandleProdProp(GenericAPIView):

    def get(self, request, prop_id):

        prop = get_object_or_404(ProductProp, id=prop_id)
        sz = ProdPropSz(prop)
        return Response({'status': 'get product prop',
                         'prop': sz.data})

    def post(self, request, prod_id):

        sz_data = {}
        sz_data.update(request.data)
        sz_data.update(product_id=prod_id)
        sz = ProdPropSz(data=sz_data)
        sz.is_valid(raise_exception=True)
        sz.save()

        return Response({'status': 'added prop to product',
                         'prop': sz.data})

    def put(self, request, prop_id):

        prop = get_object_or_404(ProductProp, id=prop_id)
        sz_data = {}
        sz_data.update(request.data)
        sz_data.update(product_id=prop.product.id)
        sz = ProdPropSz(prop, data=sz_data)
        sz.is_valid(raise_exception=True)
        sz.save()

        return Response({'status': 'updated product prop',
                         'prop': sz.data})

    def delete(self, request, prop_id):

        prop = get_object_or_404(ProductProp, id=prop_id)
        prop.delete()

        return Response({'status': 'deleted product prop'})
