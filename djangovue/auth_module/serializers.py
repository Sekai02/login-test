from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User 


class RegisterSerializers(serializers.ModelSerializer):
    password = serializers.CharField()
    
    class Meta:
        model = User
        fields = ('username','password1','password2')
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password1=validated_data['password1'],
            password2=validated_data['password2'],
            
        )