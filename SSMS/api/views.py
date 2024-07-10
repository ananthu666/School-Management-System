from django.shortcuts import render
from rest_framework import viewsets
from .models import Custom_User, Subject, Mark
from .serializers import UserSerializer, SubjectSerializer, MarkSerializer,LoginSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny

User = get_user_model()

class SingupViewSet(viewsets.ModelViewSet):
    queryset = Custom_User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    
    def list(self, request):
        return Response({'error': 'Method Not Allowed'})  

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'user': UserSerializer(user, context=self.get_serializer_context()).data,
                'message': 'User created successfully. Now perform Login to get your token',
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer
    queryset = User.objects.none()

    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'username': user.username
                }, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = Custom_User.objects.all()
    serializer_class = UserSerializer

    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    
    




class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    
    



class MarkViewSet(viewsets.ModelViewSet):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer
    
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]



