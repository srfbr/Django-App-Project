#from django.contrib.auth.models import User
#from rest_framework.response import Response
#from rest_framework import status
#from rest_framework_simplejwt.tokens import RefreshToken

#class LoginBehavior():
#    def __init__(self, data):
#        self.data = data
#
#    def verifyUser(self):
#        return User.objects.get(
#            username=self.data.get('username'),
#        )
#    
#    def run(self):
#        user = self.verifyUser()
#        if (self.verifyUser() and user.check_password(raw_password=self.data.get('password'))):
#            refresh = RefreshToken.for_user(user)
#            return Response(
#                {
#                    'status': 'Logged',
#                    'refresh': str(refresh),
#                    'access': str(refresh.access_token),
#                },
#                status=status.HTTP_200_OK
#            )