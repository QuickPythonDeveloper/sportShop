from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from ...models.productCategory import ProductCategory

from django.shortcuts import get_object_or_404


class CatAddParent(GenericAPIView):

    def post(self, request, cat_id, parent_id):

        cat = get_object_or_404(ProductCategory, id=cat_id)
        parent = get_object_or_404(ProductCategory, id=parent_id)

        cat.parent = parent
        cat.save()

        return Response({'status': 'added product category parent'})

    def delete(self, request, cat_id):

        cat = get_object_or_404(ProductCategory, id=cat_id)
        cat.parent = None
        cat.save()

        return Response({'status': 'removed product category parent'})
