from django.urls import path
from .views import home , login_user, logout_user , register_user , custromer_record , delete_record

urlpatterns = [
    path('', home ,name="home"),
    path('login/' , login_user , name='login'),
    path('logout/' , logout_user , name='logout'),
    path('register/' , register_user , name='register'),
    path('record/<int:pk>' , custromer_record , name='record'),
    path('delete_record/<int:pk>' , delete_record , name='delete_record'),
]
