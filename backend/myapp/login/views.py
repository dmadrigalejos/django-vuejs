from rest_framework import viewsets
from myapp.user.serializer import UserSerializer
from .service import LoginService
from rest_framework.response import Response
from myapp.utility.headerutil import HeaderUtil
from rest_framework.decorators import action
import json
from rest_framework import status
from django.core import serializers
class LoginView(viewsets.ViewSet):

    serializer_class = UserSerializer


    def create(self, request):
        body_unicode = request.body.decode('utf-8')

        body = json.loads(body_unicode)

        loginService = LoginService()

        user = loginService.retrieveUser(username=body['userName'],password=body['userPassword'])

        if user is not None:
            serialize = UserSerializer(instance=user[0])
            headers = HeaderUtil.info("Successfully Logged in")
            request.session['user'] = serialize.data
            return Response(serialize.data, headers=headers,content_type='application/json' , status=status.HTTP_200_OK)
        else:
            headers = HeaderUtil.error("Invalid Credentials")
            return Response(None, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='authenticate', url_name='authenticate')
    def authenticate(self, request):
        try:
            if request.session['user'] is not None:
                user = request.session['user']
                serializer = UserSerializer(instance=user)
                return Response(serializer.data, content_type='application/json', status=status.HTTP_200_OK)
        except KeyError:
            return Response(None, status=status.HTTP_400_BAD_REQUEST)


    @action(methods=['get'], detail=False, url_path='invalidate', url_name='invalidate')
    def invalidate(self, request):

        print("=======")


        try:
            del request.session['user']
        except KeyError:
            pass
        return Response(None, status=status.HTTP_200_OK)

