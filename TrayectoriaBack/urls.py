"""TrayectoriaBack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework import permissions
# from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authtoken import views

from api import views

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     re_path(r'^', include(router.urls)),
#     re_path(r'^api/v1/login/', include('Login.urls')),
#     re_path(r'^api/v1/profile/', include('Profile.urls')),
#     re_path(r'^api/v1/user/', include('User.urls')),
#     #path('api_generate_token/',views.obtain_auth_token),
# ]
router = routers.DefaultRouter()
router.register('products',views.ProductView)

urlpatterns = [
    path('admin/', admin.site.urls),
    #API_URLS
    path('api/v1/', include(router.urls)),
    #AUTH_URLS
    path('api/v1/auth/', include('rest_auth.urls')),
    path('api/v1/auth/registration/', include('rest_auth.registration.urls')),
    path('accounts/login', include('allauth.urls')),
]