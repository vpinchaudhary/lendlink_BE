from ..serializers import OTPRequestSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import status

class OTPRequestView(APIView): 
    def get(self, request):
        serializer = OTPRequestSerializer(data=request.data)

        if serializer.is_valid():
            serializer.sendOTP()
            return Response({"success": True}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)