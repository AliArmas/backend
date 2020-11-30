from rest_framework import serializers
from user import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','user','name','email','password','status']

