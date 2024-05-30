from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import UserSerializer, UserLoginSerializer,ClientSerializer
from django.contrib.auth.tokens import default_token_generator
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.utils.encoding import force_bytes
from django.shortcuts import get_object_or_404
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from rest_framework.decorators import api_view


class ClientViewset(viewsets.ModelViewSet):
    queryset = User.objects.all() 
    serializer_class = ClientSerializer



class UserRegistrationAPIView(APIView):
    serializer_class = UserSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response("Account created", status=201)
        return Response(serializer.errors, status=400)


class UserLoginAPIView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return Response("user logged  in", status=201 )
            else:
                return Response({'error': "Invalid Credentials"})
        return Response(serializer.errors, status=400)



class UserLogoutAPIView(APIView):
    def get(self, request, format=None):
        logout(request)
        return Response("User logged out")
