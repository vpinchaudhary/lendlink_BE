from ..serializers import OTPRequestSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny

class OTPRequestView(APIView): 
    permission_classes = [AllowAny]
    def get(self, request):
        serializer = OTPRequestSerializer(data=request.query_params)

        if serializer.is_valid():
            serializer.sendOTP()
            return Response({"success": True}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)