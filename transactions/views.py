from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from transactions.constans import TransactionTypE
from transactions.models import Account, Transaction
from transactions.serializers import TransactionSerializer, AccountSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionTypeE(object):
    pass


class StatsView(APIView):

    def get(self, request, *args, **kwargs):
        ""

        data = {}
        for account in Account.objects.all():
            amount_in = Transaction.objects.filter(account=account,
                                                   transaction_type=TransactionTypE.IN.value).aggregate(
                sum=Coalesce(Sum("amount"), 0))

            # agregacja z wykorzystaniem funkcji Coalesce, przyjmuje
            # co najmniej 2 pola lub wyrażenia i zwraca pierwsze, które nie jest NUllem
            amount_out = Transaction.objects.filter(account=account,
                                                    transaction_type=TransactionTypE.OUT.value).aggregate(
                sum=Coalesce(Sum("amount"), 0))

            if amount_in["sum"] and amount_out["sum"]:
                data[account.id] = {
                    'name': account.name,
                    'in': amount_in,
                    'out': amount_out,
                    'balance': amount_in["sum"] - amount_out["sum"] + account.initial_balance
                }

            # legacy code z defaultowymi warttościami 0
            # else:
            #
            #     data[account.id] = {
            #         'name': account.name,
            #         'in': 0,
            #         'out': 0,
            #         'balance': account.initial_balance
            #     }

        return Response(data=data)
