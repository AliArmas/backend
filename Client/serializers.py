from django.db.models import fields
from Client.models import ClientModel
from rest_framework import serializers

class ClientSerializers(serializers.ModelSerializer):
    class Meta :
        model = ClientModel
        fields = ('__all__')