from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.db.models import Q

from rest_framework.parsers import (MultiPartParser,
                                    FormParser)

from ....models.galleryImage import GalleryImage

from ....serializers.product.gImage import ProdGalImageSz

import os


class HandleProdGalImage(GenericAPIView):

    parser_classes = [MultiPartParser,
                      FormParser]

    def get(self, request, img_id):

        img = get_object_or_404(GalleryImage, id=img_id)
        sz = ProdGalImageSz(img)
        return Response({'status': 'get product image',
                         'image': sz.data})

    def post(self, request, prod_id):

        sz_data = {'product_id': prod_id,
                   'image': request.data['image']}
        sz = ProdGalImageSz(data=sz_data)
        sz.is_valid(raise_exception=True)
        sz.save()

        return Response({'status': 'added product image',
                         'image': sz.data})

    def delete(self, request, img_id):

        img = get_object_or_404(GalleryImage, id=img_id)
        cwd = os.getcwd()
        os.remove(cwd + img.image.url)
        img.delete()

        product = img.product
        images = GalleryImage.objects.filter(Q(format="jpg") |
                                             Q(format="jpeg"),
                                             product=product)
        txt = ""

        if images.count() < 2:
            product.insta_perm = False
            product.save()
            txt = " and removed product insta perm"

        status = "deleted product image" + txt

        return Response({'status': status})
