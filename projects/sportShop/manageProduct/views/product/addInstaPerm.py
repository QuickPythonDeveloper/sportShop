from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.db.models import Q

from manageProduct.models.defineProduct import DefineProduct
from manageProduct.models.galleryImage import GalleryImage


class ProdAddInstaPerm(GenericAPIView):

    def post(self, request, prod_id):

        product = get_object_or_404(DefineProduct, id=prod_id)
        images = GalleryImage.objects.filter(Q(format="jpg") |
                                             Q(format="jpeg"),
                                             product=product)
        if images.count() < 2:
            return Response({'status': 'Not enough jpg images'})

        product.insta_perm = True
        product.save()

        return Response({'status': 'added product insta permission'})
