from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from transactions.constans import TransactionTypE
from transactions.models import Account, Transaction
from transactions.serializers import TransactionSerializer, AccountSerializer, StatsSerializer, StatsFilterSerializer


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
        filter_serializer = StatsFilterSerializer(data=request.query_params)
        filter_serializer.is_valid(raise_exception=True)

        from_date = filter_serializer.validated_data.get("from_date")
        to_date = filter_serializer.validated_data.get("to_date")

        transaction_qs = Transaction.objects.filter(created__gte=from_date, created__lte=to_date)
        data = []

        for account in Account.objects.all():
            data.append(
                {"id": account.id,
                 "name": account.name,
                 'account_in': account.amount_in(transaction_qs=transaction_qs),
                 'account_out': account.amount_out(transaction_qs=transaction_qs),
                 'balance': account.balance(transaction_qs=transaction_qs),
                 }
            )

        # serializer = StatsSerializer(instance=Account.objects.all(), many=True)

        response_data = {"results": data, "date": {"from": from_date.isoformat(), "to": to_date.isoformat()}}

        return Response(data=response_data)

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
