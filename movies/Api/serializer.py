from rest_framework import serializers
from .models import Movielist
from django.contrib.auth.models import User


class MovieSerializer(serializers.Serializer):
    name=serializers.CharField()
    year=serializers.IntegerField()
    director=serializers.CharField()
    genre=serializers.CharField()
    
class MovieModelSer(serializers.ModelSerializer):
    class Meta:
        model=Movielist
        fields="__all__"
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","password","email"]
    def create(self, validated_data):
        print(validated_data)
        return User.objects.create_user(**validated_data)
        