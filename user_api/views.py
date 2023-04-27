from django.contrib.auth import get_user_model, login ,logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegisterSerializer,UserLoginSerializer,UserSerializer

from rest_framework import permissions,status
from .validations import custom_validation,validate_password,validate_username
class UserRegister(APIView):
    permission_classes=(permissions.AllowAny,)
    def post(self,request):
        clean_data=custom_validation(request.data)
        serializer = UserRegisterSerializer(data=clean_data)
        if serializer.is_valid():
            user = serializer.create(clean_data)
            if user:
                return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserLogin(APIView):
    permission_classes=(permissions.AllowAny,)
    authentication_classes=(SessionAuthentication,)

    def post(self,request):
        data=request.data
        print(data)
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.check_user(data)
            print(data)
            login(request,user)
            return Response(serializer.data,status=status.HTTP_200_OK)

class UserLogout(APIView):
    def get(self,request):
        logout(request)
        return Response(status=status.HTTP_200_OK)

class UserView(APIView):
    permission_classes=(permissions.IsAuthenticated,)
    authentication_classes=(SessionAuthentication,)

    def get(self,request):
        user = request.user
        serializer = UserSerializer(user)
        return Response({'user':serializer.data},status=status.HTTP_200_OK)