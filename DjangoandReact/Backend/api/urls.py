from django.urls import path 
from .views import CreateNoteView , DeleteNoteView
urlpatterns = [
    path('note/create/',CreateNoteView.as_view(), name='create-note'),
    path('note/delete/<int:pk>' , DeleteNoteView.as_view() , name='delete-note'),
]
