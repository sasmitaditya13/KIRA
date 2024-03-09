from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path,include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)

urlpatterns = [
    path('',views.index),
    path('',include(router.urls)),
    path('login', views.UserLoginView.as_view())
]
