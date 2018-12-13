from rest_framework import serializers
from .models import User

class UserSerializer(serializers.Serializer):
    userId = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=256)
    #userPassword = serializers.CharField(max_length=256)
    userFirstname = serializers.CharField(max_length=256)
    userLastname = serializers.CharField(max_length=256)
