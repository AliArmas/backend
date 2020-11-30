from django.db.models import fields
from Profile.models import ProfileModel
from rest_framework import serializers

class ProfileSerializers(serializers.ModelSerializer):
    class Meta :
        model = ProfileModel
        fields = ('__all__')