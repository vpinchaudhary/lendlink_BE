from rest_framework import serializers
from django.contrib.auth.models import User
from ..models import OtpModel
from django.core.mail import send_mail

class OTPVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()
    purpose = serializers.CharField()
    
    def validate(self, data):
        try:
            otp_obj = OtpModel.objects.get(email=data['email'], otp=data['otp'], purpose=data['purpose'])
            # Check if OTP has expired
            if not otp_obj.is_valid():
                raise serializers.ValidationError("OTP has expired.")
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid user email.")
        except OtpModel.DoesNotExist:
            raise serializers.ValidationError("Invalid OTP.")
        return data
    
class OTPRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()
    purpose = serializers.CharField()

    def validate(self, data):
        purpose = data['purpose']
        if purpose not in ["PWD", "REG"]:
            raise serializers.ValidationError("Invalid Purpose")
        
        return data
    
    def sendOTP(self):
        otp_obj = OtpModel.create_otp_for_email(self.validated_data['email'], self.validated_data['purpose'])
        send_mail(
            'Your Forgot Password OTP',
            f'Your OTP is: {otp_obj.otp}',
            'noreply@yourdomain.com',  # From address
            [self.validated_data['email']],  # Recipient list
            fail_silently=False,
        )