from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, NoteSerializer , LoginSerializer
from rest_framework import status
from .models import Note
from rest_framework.permissions import IsAuthenticated 
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
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

class LoginAPI(APIView):
    def post(self, request):
        data = request.data
        username = request.data.get('username')
        password = request.data.get('password')
        serializer = LoginSerializer(data=data)
        if serializer.is_valid():
            print(serializer.data)
            
            
            user = authenticate(username = username,password= password)
            print("######")
            print(user)
            if user:
                token,_ = Token.objects.get(user = user)
                return Response({'token':token})
        return Response(serializer.errors)


class NoteAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        data['user'] = request.user.id
        
        serializer = NoteSerializer(data=data)

        if serializer.is_valid():
            serializer.save() 
            
            print(serializer.data)
            return Response({'note': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'errors': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def get(self, request):
        notes = Note.objects.all()
        serializer = NoteSerializer(notes , many=True)
        if serializer.data:
            return Response({'data':serializer.data} , status=status.HTTP_200_OK)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_204_NO_CONTENT)


        