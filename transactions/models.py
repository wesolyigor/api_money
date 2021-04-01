from django.db import models

from transactions.constans import TransactionTypE


class Account(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, null=True, blank=True)
    initial_balance = models.DecimalField(max_digits=10, decimal_places=2)


class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=250, null=True, blank=True)
    transaction_type = models.SmallIntegerField(choices=[(
        transaction_type.value, transaction_type.name) for transaction_type in TransactionTypE
    ])
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
