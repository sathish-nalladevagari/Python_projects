from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, NoteSerializer
from rest_framework import status
from .models import Note
# Create your views here.


class Index(APIView):
    def get(self , request):
        return Response({'kei' : 'hello'})



class RegisterAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'user' : serializer.data} , status=status.HTTP_200_OK)
        return Response({'err' : serializer.errors})


class NoteAPI(APIView):
    def post(self , request):
        data = request.data
        serializer = NoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'note' : serializer.data} , status=status.HTTP_201_CREATED)
        return Response({'errors' : serializer.errors} , status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def get(self, request):
        notes = Note

        