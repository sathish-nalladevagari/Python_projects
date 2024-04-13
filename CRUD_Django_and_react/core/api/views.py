from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import UserSerializer , NoteSerializer
from django.contrib.auth.models import User
from .models import Note
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class Index(APIView):
    def get(self , request):
        return Response({'kei' : 'hello'})


class UserAPI(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class NoteAPI(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)
        except Exception as e:
            return Response({'error': str(e)})
        
class GetNoteAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    

