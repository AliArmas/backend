from django.urls import path,re_path
from Client import views

urlpatterns = [
    re_path(r'^',views.ClientViewSet.as_view())
]