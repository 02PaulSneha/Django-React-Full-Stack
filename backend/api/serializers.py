from django.contrib.auth.models import User # This model stores user details like username, password etc.
from rest_framework import serializers # Django REST Framework (DRF).Python objects (like User) into JSON format and vice versa.
from .models import Note

class UserSerializer(serializers.ModelSerializer):
    class Meta: # This tells Django which model to serialize and which fields to include.
        model = User #Specifies that this serializer is for the User model.
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data) #**validated_data → Spreads the dictionary into keyword arguments (username="John", password="1234", etc.).
        return user
        
        
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields =  ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}
        
