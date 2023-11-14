from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class CreatedByUserMixin(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="%(class)s_created")

    class Meta:
        abstract = True

class TransactionType(models.TextChoices):
    LEND = 'LEND', _('Lend')
    BORROW = 'BORROW', _('Borrow')

class Address(CreatedByUserMixin):
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.address

class Person(CreatedByUserMixin):
    name = models.CharField(max_length=100)
    address = models.ForeignKey(Address, related_name='residents', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class FinancialTransaction(CreatedByUserMixin):
    person = models.ForeignKey(Person, related_name='financial_transactions', on_delete=models.CASCADE)
    duration = models.IntegerField()
    rate = models.FloatField()
    amount = models.IntegerField()
    type = models.CharField(max_length=10, choices=TransactionType.choices)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} - {self.amount} - {self.person.name}"

class PaymentModel(CreatedByUserMixin):
    financial_transaction = models.ForeignKey(FinancialTransaction, related_name='payment_details', on_delete=models.CASCADE)
    paid_amount = models.IntegerField()

    def __str__(self):
        return f"{self.financial_transaction} - Paid Amount: {self.paid_amount}"

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"
