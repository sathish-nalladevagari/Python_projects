from home.views import index , home , person , LoginAPI , RegisterAPI
from django.urls import path

urlpatterns = [
    path("index/",index ),
    path('',home),
    path('person/', person),
    path('login/', LoginAPI.as_view()),
    path('register/',RegisterAPI.as_view())
]