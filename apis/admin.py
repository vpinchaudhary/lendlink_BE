from django.contrib import admin

from .models import OtpModel, Address, FinancialTransaction, Person, PaymentModel

# Register your models here.
admin.site.register(OtpModel)
admin.site.register(Address)
admin.site.register(FinancialTransaction)
admin.site.register(Person)
admin.site.register(PaymentModel)
