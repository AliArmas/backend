from django.urls import path,re_path
from Profile import views

urlpatterns = [
    re_path(r'^profile',views.ProfileViewSet.as_view())
]