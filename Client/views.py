from django.shortcuts import render   
from django.shortcuts import get_object_or_404
from django.http import Http404,HttpResponse,HttpRequest
from rest_framework.response import Response
from rest_framework.views import APIView

#modelos
from Client.models import ClientModel
#serializers 
from Client.serializers import ClientSerializers
#vistas
class ClientViewSet(APIView):
    
    def post(self,request,format=None):
        serializer = ClientSerializers(data=request.data, context={'request':request})
        if(serializer.is_valid()):
            serializer.save()
            return "echo"
