from django.urls import path 
from .views import Index , UserAPI , NoteAPI , GetNoteAPI

from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView 
urlpatterns = [
    path("", Index.as_view() , name="index"),
    path("register/" , UserAPI.as_view() , name="register"),
    path("token/" , TokenObtainPairView.as_view() , name="token"),
    path("token/refresh/" , TokenRefreshView.as_view() , name="refresh"),
    path("todos/" , NoteAPI.as_view() , name="notes"),
    path("todos/<int:pk>/" , GetNoteAPI.as_view() , name="notes_api"),
]
