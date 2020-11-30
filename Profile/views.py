from django.shortcuts import render   
from django.shortcuts import get_object_or_404
from django.http import Http404,HttpResponse,HttpRequest
from rest_framework.response import Response
from rest_framework.views import APIView

#modelos
from Profile.models import ProfileModel
#serializers 
from Profile.serializers import ProfileSerializers
#vistas
class ProfileViewSet(APIView):
    
    def post(self,request,format=None):
        serializer = ProfileSerializers(data=request.data, context={'request':request})
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)