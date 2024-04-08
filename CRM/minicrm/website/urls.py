from django.urls import path
from .views import home , login_user, logout_user , register_user , custromer_record , delete_record , add_customer, update_record

urlpatterns = [
    path('', home ,name="home"),
    path('login/' , login_user , name='login'),
    path('logout/' , logout_user , name='logout'),
    path('register/' , register_user , name='register'),
    path('record/<int:pk>' , custromer_record , name='record'),
    path('delete_record/<int:pk>' , delete_record , name='delete_record'),
    path('add_customer' , add_customer , name='add_customer'),
    path('update/<int:pk>',update_record , name='update' ),
]
