from decimal import Decimal

from django.db import models
from django.db.models import Sum
from django.db.models.functions import Coalesce

from transactions.constans import TransactionTypE


class Account(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, null=True, blank=True)
    initial_balance = models.DecimalField(max_digits=10, decimal_places=2)

    def amount_in(self, transaction_qs=None):

        if transaction_qs is None:
            transaction_qs = Transaction.objects.all()

        amount_in = transaction_qs.filter(account=self,
                                          transaction_type=TransactionTypE.IN.value).aggregate(
            sum=Coalesce(Sum("amount"), 0))
        return amount_in["sum"] or Decimal(0)

    def amount_out(self, transaction_qs=None):

        if transaction_qs is None:
            transaction_qs = Transaction.objects.all()

        amount_out = transaction_qs.filter(account=self,
                                           transaction_type=TransactionTypE.OUT.value).aggregate(
            sum=Coalesce(Sum("amount"), 0))
        return amount_out["sum"] or Decimal(0)

    def balance(self, transaction_qs=None):
        return self.amount_in(transaction_qs=transaction_qs) - \
               self.amount_out(transaction_qs=transaction_qs) + \
               self.initial_balance

    def __str__(self):
        return self.name


class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=250, null=True, blank=True)
    transaction_type = models.SmallIntegerField(choices=[(
        transaction_type.value, transaction_type.name) for transaction_type in TransactionTypE
    ])
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}_{self.description}_{self.amount}"
