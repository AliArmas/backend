from django.urls import path,re_path
from User import views

# urlpatterns = [
#     re_path(r'^(?P<pk>[0-9]+)$',views.UserViewSet.as_view())
# ]
# #
urlpatterns = [
    re_path(r'^register/', views.UserViewSet.as_view()),
    #path('get', views.UserViewSet.as_view()),
    #path('delete/<slug:id>', views.UserViewSet.as_view()),
    #path('edit/<slug:id>', views.UserViewSet.as_view())
]