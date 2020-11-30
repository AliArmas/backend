from django.shortcuts import render

from django.shortcuts import render
from .models import User
from models.user.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView 
import json
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from django.http import HttpResponse
#
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = permissions.IsAuthenticated


    # def post(self,request,format=None):
    #         user_data = JSONParser().parse(request)
    #         user_serializer = UserSerializer(data=user_data, contex={'request':request})
    #         if user_serializer.is_valid():
    #             user_serializer.save()
    #             return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED) 
    #         return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        