from django.shortcuts import render
from rest_framework import viewsets

from transactions.models import Account, Transaction
from transactions.serializers import TransactionSerializer, AccountSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
