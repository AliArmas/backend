from django.urls import path, re_path
from django.conf.urls import include
from Login.views import CustomAuthToken

urlpatterns = [
    re_path(r'^', CustomAuthToken.as_view()),
]