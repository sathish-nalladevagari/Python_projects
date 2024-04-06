from django.urls import path
from .views import index , login_user, logout_user

urlpatterns = [
    path('', index ,name="home"),
    path('login/' , login_user , name='login'),
    path('logout/' , logout_user , name='logout'),
]
 