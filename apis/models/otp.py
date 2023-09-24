from django.db import models
import random
from datetime import datetime, timedelta
from django.utils import timezone

class OtpModel(models.Model):
    email = models.EmailField()
    otp = models.CharField(max_length=6, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField()
    PURPOSE_CHOICES = [
        ('REG', 'Registration'),
        ('PWD', 'Password Reset'),
    ]
    purpose = models.CharField(max_length=3, choices=PURPOSE_CHOICES)

    @classmethod
    def generate_otp(cls):
        """Generate a 6-digit OTP."""
        return str(random.randint(100_000, 999_999))

    @classmethod
    def create_otp_for_email(cls, email, purpose):
        otp_str = cls.generate_otp()
        expiry_date = datetime.now() + timedelta(minutes=10)  # OTP is valid for 10 minutes
        otp_obj = cls.objects.create(email=email, otp=otp_str, expiry_date=expiry_date, purpose=purpose)
        otp_obj.save()

        return otp_obj

    def is_valid(self):
        """Check if the OTP is valid (i.e., not expired)."""
        now = timezone.now()  # Use Django's timezone-aware datetime
        return now < self.expiry_date

    def __str__(self):
        return f"OTP: {self.otp} for {self.email} ({self.purpose})"
