
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {"password" : { "write_only" : True}}

   
    def create(self, validated_data):
        return super().create(validated_data)
    
    

    
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id','title','desc']
        extra_kwargs = {'user' : {'read_only' : True}}

    