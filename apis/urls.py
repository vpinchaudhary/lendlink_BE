from django.urls import path
from .views import (
    AddressList,
    AddressDetail,
    PersonList,
    PersonDetail,
    FinancialTransactionList,
    FinancialTransactionDetail,
    PaymentModelList,
    PaymentModelDetail,
    RegisterView,
    OTPRequestView,
    CustomTokenObtainPairView,
    MeAPIView
)
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('refresh-token/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name="register"),
    path('get-otp/', OTPRequestView.as_view(), name="get-otp"),
    path('me/', MeAPIView.as_view(), name="me"),
    
    # Address URLs
    path('addresses/', AddressList.as_view(), name='address-list'),
    path('addresses/<int:pk>/', AddressDetail.as_view(), name='address-detail'),
    
    # Person URLs
    path('people/', PersonList.as_view(), name='person-list'),
    path('people/<int:pk>/', PersonDetail.as_view(), name='person-detail'),
    
    # FinancialTransaction URLs
    path('financial-transactions/', FinancialTransactionList.as_view(), name='financialtransaction-list'),
    path('financial-transactions/<int:pk>/', FinancialTransactionDetail.as_view(), name='financialtransaction-detail'),
    
    # PaymentModel URLs
    path('payments/', PaymentModelList.as_view(), name='paymentmodel-list'),
    path('payments/<int:pk>/', PaymentModelDetail.as_view(), name='paymentmodel-detail'),
]
