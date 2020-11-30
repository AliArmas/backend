from django.conf.urls import url,re_path
from django.urls import include
from rest_framework.routers import DefaultRouter
from user.views import UserViewSet

router = DefaultRouter()
router.register('user',UserViewSet)

urlpatterns = [
    url(r'^user', include(router.urls)),
]