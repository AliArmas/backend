from django.urls import path,re_path
from User import views

# urlpatterns = [
#     re_path(r'^(?P<pk>[0-9]+)$',views.UserViewSet.as_view())
# ]
# #
urlpatterns = [
    re_path(r'^user', views.UserViewSet.as_view()),
    path('user_get', views.UserViewSet.as_view()),
    path('user_delete/<slug:id>', views.UserViewSet.as_view()),
    path('user_edit/<slug:id>', views.UserViewSet.as_view())
]