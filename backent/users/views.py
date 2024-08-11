from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.permissions import IsAuthenticated

from . serializers import UserCreateSerializer, UserSerializer

class RegisterView(APIView):
    def post(self,request):
        serializer=UserCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        user=serializer.create(serializer.validated_data)
        user = UserSerializer(user)

        return Response({"user":user.data, "status_code":"201","status":"CREATED","Description":"congratulations Your Account is Created Successfully !!"} ,status=status.HTTP_201_CREATED)

class RetriveView(APIView):
    def get(self,request):
        # permission_classes=[permissions.IsAthenticated]
        permission_classes = [IsAuthenticated]
        user=request.user
        user=UserSerializer(user)
        return Response({"user":user.data, "status_code":"200","status": "OK"},status=status.HTTP_200_OK)

