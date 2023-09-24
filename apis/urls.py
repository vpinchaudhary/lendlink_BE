from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import RegisterView, OTPRequestView

urlpatterns = [
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='login'),
    path('refresh-token/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name="register"),
    path('get-otp/', OTPRequestView.as_view(), name="get-otp")
]
