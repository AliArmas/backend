from django.db.models import fields
from User.models import UserModel
from rest_framework import serializers

class UserSerializers(serializers.ModelSerializer):
    class Meta :
        model = UserModel
        fields = ('__all__')