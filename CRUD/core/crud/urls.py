from django.urls import path
from .views import index , register_user , login_user , logout_user , add_task , update_task

urlpatterns = [
    path('', index , name='home'),
    path('register/', register_user , name='register'),
    path('login/', login_user , name='login'),
    path('logout/', logout_user , name='logout'),
    path('logout/', logout_user , name='logout'),
    path('addtask/', add_task , name='add'),
    path('updatetask/<int:pk>', update_task , name='update'),
]