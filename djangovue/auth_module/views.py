from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import response,status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .serializers import LoginSerializers,RegisterSerializers

def home(request):
    return HttpResponse("Welcome to the Django Vue Authentication Module")

class RegisterView(APIView):
    permission_classes = []
    def post(self,request):
        serializer = RegisterSerializers(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return response.Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = []
    def post(self,request):
        serializer = LoginSerializers(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)
            return response.Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'message': 'Login successful'
            }, status=status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProtectedView(APIView):
    def get(self, request):
        return response.Response({'message': 'This is a protected view, you need to login to access the view'}, status=status.HTTP_200_OK)