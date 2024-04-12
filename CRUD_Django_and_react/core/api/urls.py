from django.urls import path 
from .views import Index , RegisterAPI , NoteAPI, LoginAPI
urlpatterns = [
    path("", Index.as_view() , name="index"),
    path("register/", RegisterAPI.as_view() , name="register" ),
    path("login/", LoginAPI.as_view() , name="login" ),
    
    path("notes/", NoteAPI.as_view() , name="notes" ),
]
