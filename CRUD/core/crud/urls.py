from django.urls import path
from .views import index , register_user , login_user

urlpatterns = [
    path('', index , name='home'),
    path('register/', register_user , name='register'),
    path('login/', login_user , name='login'),
]