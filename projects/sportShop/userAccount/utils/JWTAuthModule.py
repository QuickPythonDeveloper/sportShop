from rest_framework.serializers import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken


class JWTAuthModule:

    def __init__(self, username, password, userClass):

        self.username = username
        self.password = password
        self.userClass = userClass
        self.status = None

    def check_user(self):

        users = self.userClass.objects.filter(username=self.username)

        if users.exists():

            user = users[0]
            if user.check_password(self.password):

                refresh = RefreshToken.for_user(user)
                self.status = 'logged in'

                return {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token)
                }

            self.status = 'wrong'
            raise ValidationError({'error': 'Wrong password'})

        self.status = 'wrong'
        raise ValidationError({'error': 'Username not found'})
