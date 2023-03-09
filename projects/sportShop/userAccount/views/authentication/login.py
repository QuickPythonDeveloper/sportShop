from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from userAccount.utils.JWTAuthModule import JWTAuthModule

from userAccount.models.customerUser import CustomerUser


class UserLogin(GenericAPIView):

    def post(self, request):

        auth_init = JWTAuthModule(request.data['username'],
                                  request.data['password'],
                                  CustomerUser)

        tokens = auth_init.check_user()

        return Response({'status': 'logged in',
                         'tokens': tokens})
