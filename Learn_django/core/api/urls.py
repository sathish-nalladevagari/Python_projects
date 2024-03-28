from home.views import index , home , person , login
from django.urls import path

urlpatterns = [
    path("index/",index ),
    path('',home),
    path('person/', person),
    path('login/',login)
]