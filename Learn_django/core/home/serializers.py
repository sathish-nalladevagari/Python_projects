from rest_framework import serializers
from .models import Person , Color



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = ["color_name"]

class PeopleSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    class Meta:
        model = Person
        fields = '__all__'
        # depth = 1
    
    def validate(self, data):
        special_characters = "!@#$%^&*()_+-<>?|"
        if any(char in special_characters for char in data['name']):
            raise serializers.ValidationError("Name should not contain special characters")
        
        if data['age'] < 18:
            raise serializers.ValidationError("age should be greater than 18")
        return data
    
    
        
        
