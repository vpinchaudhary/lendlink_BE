from rest_framework.response import Response
from ..serializers import RegisterSerializer
from rest_framework.views import APIView
from rest_framework import status

#Register API
from rest_framework import status

class RegisterView(APIView):
    def post(self, request):
        register_serializer = RegisterSerializer(data=request.data)
        if register_serializer.is_valid():
            response_data = register_serializer.save()
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(register_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
