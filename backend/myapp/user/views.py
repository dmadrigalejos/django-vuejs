from rest_framework import viewsets
from rest_framework.response import Response
from .serializer import UserSerializer
import json
from rest_framework.decorators import action
from .service import UserService
from myapp.utility.headerutil import HeaderUtil
from rest_framework import status
#from rest_framework.permissions import IsAuthenticated


class UserView(viewsets.ViewSet):
    serializer_class = UserSerializer
 #   permission_classes = (IsAuthenticated)

    def create(self, request):
        userService = UserService()
        body_unicode = request.body.decode('utf-8')
        #simple json loads
        body = json.loads(body_unicode)
        userService.createUser(body)
        headers = HeaderUtil.success("User created successfully")
        return Response(None, headers=headers,  status=status.HTTP_200_OK)

    def update(self, request, pk):
        userService = UserService()
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        affcted_row = userService.updateUser(body, pk)
        if (affcted_row <= 0):
            headers = HeaderUtil.error("ID doesn't Exist")
            return Response(None, headers=headers,status=status.HTTP_400_BAD_REQUEST)
        else:
            headers = HeaderUtil.error(str(affcted_row) + " record(s) updated.")
            return  Response(None,headers=headers, status=status.HTTP_200_OK)


    def list(self, request):
        userService = UserService()
        serializer = UserSerializer(instance=userService.retrieveUsers(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    @action(methods=['post'], detail=False, url_path='update', url_name='update')
    def getOne(self, request):
        userService = UserService()
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        user = userService.retrieveOneUser(body['userId'])
        if len(user) > 0:
            serialize = UserSerializer(instance=user[0])
            return Response(serialize.data)
        else:
            headers = HeaderUtil.error("ID doesn't Exist")
            return Response(None,headers=headers,status=status.HTTP_400_BAD_REQUEST)

