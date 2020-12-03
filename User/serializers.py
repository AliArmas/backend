from rest_framework import serializers
from User.models import UserModel

class UserSerializers(serializers.ModelSerializer):
    class Meta :
        model = UserModel
        fields = ('__all__')
    # class Meta:
    #     model = User
    #     fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email']
    #     extra_kwargs = {'password': {'write_only': True}}

    #     def create(self, validated_data):
        
    #         user = User(
    #             email=validated_data['email'],
    #             username=validated_data['username']
    #         )

    #         user.set_password(validated_data['password'])
    #         user.save()

    #         return user