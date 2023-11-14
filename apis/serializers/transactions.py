from rest_framework import serializers
from ..models import Address, Person, FinancialTransaction, PaymentModel

class CreatedByUserSerializerMixin(serializers.ModelSerializer):
    class Meta:
        abstract = True
        read_only_fields = ('creator',)

class AddressSerializer(CreatedByUserSerializerMixin, serializers.ModelSerializer):
    class Meta(CreatedByUserSerializerMixin.Meta):
        model = Address
        fields = '__all__'

class PersonSerializer(CreatedByUserSerializerMixin, serializers.ModelSerializer):
    address = AddressSerializer(read_only=True)
    address_id = serializers.PrimaryKeyRelatedField(
        queryset=Address.objects.all(),
        write_only=True,
        source='address'
    )

    class Meta(CreatedByUserSerializerMixin.Meta):
        model = Person
        fields = '__all__'
        extra_kwargs = {
            'person': {'write_only': True},
        }


class FinancialTransactionSerializer(CreatedByUserSerializerMixin, serializers.ModelSerializer):
    person = PersonSerializer(read_only=True)
    person_id = serializers.PrimaryKeyRelatedField(
        queryset=Person.objects.all(),
        write_only=True,
        source='person'
    )

    class Meta(CreatedByUserSerializerMixin.Meta):
        model = FinancialTransaction
        fields = '__all__'
        extra_kwargs = {
            'person': {'write_only': True},
        }

class PaymentModelSerializer(CreatedByUserSerializerMixin, serializers.ModelSerializer):
    class Meta(CreatedByUserSerializerMixin.Meta):
        model = PaymentModel
        fields = '__all__'
