from django.urls import path 
from .views import Index , RegisterAPI
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView
urlpatterns = [
    path("", Index.as_view() , name="index"),
    path("register/", RegisterAPI.as_view() , name="register" ),
    path("token/", TokenObtainPairView.as_view() , name="token" ),
    path("token/refresh/", TokenRefreshView.as_view() , name="refresh" ),
]
