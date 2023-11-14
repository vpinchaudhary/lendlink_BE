from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..serializers import UserSerializer

class MeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Serialize the user object
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
