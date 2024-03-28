from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import Person
from .serializers import PeopleSerializer , LoginSerializer

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

@api_view(['POST'])
def login(request):
    data = request.data
    serializer = LoginSerializer(data=data)
    if serializer.is_valid():
        data = serializer.validated_data
        print(data)
        return Response({'message' : 'success'})
    return Response(serializer.errors)
