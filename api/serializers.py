from .models import Product
from rest_framework import serializers

#Serializers

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'