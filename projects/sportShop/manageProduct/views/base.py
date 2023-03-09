from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


class BaseView(GenericAPIView):

    def get(self, request):

        return Response({'status': 'coming soon'})
