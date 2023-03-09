from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from ...serializers.category.allCat import AllProdCatSz

from ...models.productCategory import ProductCategory


class ProductCatList(GenericAPIView):

    def get(self, request):

        cats = ProductCategory.objects.all()
        serializer = AllProdCatSz(cats, many=True)

        return Response({'status': 'get product category list',
                         'cats': serializer.data})
