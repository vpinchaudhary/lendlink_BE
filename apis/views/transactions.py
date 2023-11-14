from rest_framework import generics, viewsets, permissions
from ..models import Address, Person, FinancialTransaction, PaymentModel
from ..serializers import AddressSerializer, PersonSerializer, FinancialTransactionSerializer, PaymentModelSerializer

# Define a mixin class for common behavior
class OwnedByUserMixin:
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(creator=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class AddressList(OwnedByUserMixin, generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressDetail(OwnedByUserMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class PersonList(OwnedByUserMixin, generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonDetail(OwnedByUserMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class FinancialTransactionList(OwnedByUserMixin, generics.ListCreateAPIView):
    queryset = FinancialTransaction.objects.all()
    serializer_class = FinancialTransactionSerializer


class FinancialTransactionDetail(OwnedByUserMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = FinancialTransaction.objects.all()
    serializer_class = FinancialTransactionSerializer


class PaymentModelList(OwnedByUserMixin, generics.ListCreateAPIView):
    queryset = PaymentModel.objects.all()
    serializer_class = PaymentModelSerializer


class PaymentModelDetail(OwnedByUserMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = PaymentModel.objects.all()
    serializer_class = PaymentModelSerializer

