from rest_framework import status
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

#modelos
from User.models import UserModel
#serializers 
from User.serializers import UserSerializers
#vistas
class UserViewSet(APIView):
    serializer_class = UserSerializers
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly)
    #permission_classes = permissions.IsAuthenticated
    # def post(self,request,format=None):
    #     serializer = UserSerializers(data=request.data)
    #     if(serializer.is_valid()):
    #         serializer.save()
    #         return Response(serializer.data,status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    # def detail(request, pk):
    #     try: 
    #         client = UserModel.objects.get(pk=pk) 
    #     except UserModel.DoesNotExist: 
    #         return JsonResponse({'message': 'The client does not exist'}, status=status.HTTP_404_NOT_FOUND)

    #     if request.method == 'GET': 
    #         serializer =   UserSerializers(client) 
    #         return JsonResponse(serializer.data)
    #     elif request.method == 'PUT': 
    #         client_data = JSONParse().parse(request) 
    #         serializer = UserSerializers(client, data=client_data) 
    #         if serializer.is_valid(): 
    #             serializer.save() 
    #             return JsonResponse(serializer.data) 
    #         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    #     elif request.method == 'DELETE': 
    #         client.delete() 
    #         return JsonResponse({'message': 'Client was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    def post(self, request, format=None):
        serializer =  UserSerializers(data = request.data, context = {'request': request})
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        user = UserModel.objects.all()
        serializer = UserSerializers(user, many= True)
        return Response(serializer.data)

    def delete(self, request, id):
        user = UserModel.objects.get(id=id)
        if(user.delete()):
            return Response(serializers.errors,status=status.HTTP_200_OK)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self, resquest, id):
        user = UserModel.objects.get(id=id)
        serializer =UserSerializers(user, data=resquest.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializers.errors,status=status.HTTP_200_OK)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)