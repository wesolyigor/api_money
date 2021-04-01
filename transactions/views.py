from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from transactions.constans import TransactionTypE
from transactions.models import Account, Transaction
from transactions.serializers import TransactionSerializer, AccountSerializer, StatsSerializer


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
        serializer = StatsSerializer(instance=Account.objects.all(), many=True)
        return Response(data={"statistics":serializer.data})


        ""

        # data = {}
        # for account in Account.objects.all():
        #     data[account.id] = {
        #         'name': account.name,
        #         'in': account.amount_in(),
        #         'out': account.amount_out(),
        #         'balance': account.balance()
        #     }

        # legacy code z defaultowymi warttościami 0
        # else:
        #
        #     data[account.id] = {
        #         'name': account.name,
        #         'in': 0,
        #         'out': 0,
        #         'balance': account.initial_balance
        #     }

