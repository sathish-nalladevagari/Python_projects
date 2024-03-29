from rest_framework.decorators import api_view , permission_classes , authentication_classes
from rest_framework.response import Response
from home.models import Person
from .serializers import PeopleSerializer , LoginSerializer , RegisterSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


@api_view(['GET', 'POST'])
def index(request):
    courses = { 
        'courses':"Python",
        'learn': ['flask', 'django', 'sathish']
    }
    if request.method == 'GET':
        print("You hit a get mehtod")
        return Response(courses)

    elif request.method == 'POST':
        print("you hit a post method")
        return Response(courses)


@api_view(['GET'])
def home(request):
    data = {
        'message': 'hello world'
    }
    return Response(data)

@api_view(["GET",'POST','PUT', 'PATCH', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def person(request):
    if request.method == 'GET':
        objs = Person.objects.filter(color__isnull = False)
        serializer = PeopleSerializer(objs, many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'PUT':
        data = request.data
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'PATCH':
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serializer = PeopleSerializer(obj, data=data , partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    else:
        data = request.data
        obj = Person.objects.get(id = data['id'])
        obj.delete()
        return Response({'message': 'Delete success'})

# Login api
class LoginAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)
        if not serializer.is_valid():
            return Response({
                'status' : False,
                'message' : serializer.errors}
                )
        user = authenticate(username = serializer.data['username'], password = serializer.data['password'] )
        if not user:
            return Response({
                'status' : False,
                'message' : "invalid credetials"
            })

        token , _= Token.objects.get_or_create(user = user)
        return Response({
            'status' : True,
            'message' : "user logged in ",
            "token" : str(token)
        })


# Register Api

class RegisterAPI(APIView):
    
    def post(self,request):
        data = request.data
        serializer = RegisterSerializer(data= data)
        if not serializer.is_valid():
            return Response({
                "status" : False,
                "message" : serializer.errors
            })
        
        serializer.save()
        return Response({
            'status' : True,
            'message' : "user created"
        })
