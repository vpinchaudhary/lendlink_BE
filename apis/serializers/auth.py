from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class RegisterSerializer(serializers.Serializer):
    permission_classes = [AllowAny]

    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, required=True, min_length=8)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    otp = serializers.CharField()
    purpose = serializers.CharField()

    def validate(self, data):
        otp_serializer = OTPVerificationSerializer(data=data)

        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        
        if len(data['password']) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        
        if not otp_serializer.is_valid():
            raise serializers.ValidationError(otp_serializer.errors)

        return data
        

    def save(self):
        """Create a User instance, but don't save it yet. Instead, generate and send OTP."""
        user = User(
            username=self.validated_data['email'],  # Here we use email as the username, you can adjust if needed.
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
        )
        user.set_password(self.validated_data['password'])
        user.save()

        refresh = RefreshToken.for_user(user)

        return {
            'user': {
                'id': user.id,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
            },
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh),
        }
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = data.pop('refresh')
        data['refresh_token'] = refresh

        access = data.pop('access')
        data['access_token'] = access

        data.update({
            'user': {
                'id': self.user.id,
                'first_name':self.user.first_name,
                'last_name': self.user.last_name,
                'email': self.user.email,
            }
        })

        return data