from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from django.db.utils import IntegrityError
from rest_framework.permissions import AllowAny

class RegisterSerializer(serializers.ModelSerializer):
    permission_classes = [AllowAny]
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate_password(self, value):
        # Validate the password
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        return value

    def validate_email(self, value):
        # Check the email format
        if not value or "@" not in value:
            raise serializers.ValidationError("Provide a valid email address.")
        
        # Ensure email is unique (although most configurations of the User model ensure this, it's still good practice)
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        
        return value

    def create(self, validated_data):
        try:
            user = User.objects.create_user(
                username=validated_data['username'],
                email=validated_data['email'],
                password=validated_data['password'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name']
            )
            return user
        except IntegrityError:
            raise ValidationError({"username": "A user with this username already exists."})
