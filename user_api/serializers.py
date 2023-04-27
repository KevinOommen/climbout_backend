from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError
User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
    def create(self,clean_data):
        userobj = User.objects.create(
            username=clean_data['username'],
            password=clean_data['password']
        )
        userobj.username =clean_data['username']
        userobj.save()
        return userobj
class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def check_user(self,clean_data):
        user=authenticate(
            username="IronMan",
            password="ironman123"
        )
        print(clean_data)
        if not user:

            raise ValidationError('Invalid Credentials 123')
        
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'username', 'password']


