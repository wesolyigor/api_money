from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from transactions.handlers import AccountAggregator
from transactions.models import Account, Transaction
from transactions.serializers import TransactionSerializer, AccountSerializer, StatsFilterSerializer, StatsSerializer


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

        aggregator = AccountAggregator(
            from_date=filter_serializer.validated_data.get("from_date"),
            to_date=filter_serializer.validated_data.get("to_date")
        )

        print(aggregator.aggregate_data)

        data = aggregator.aggregate_data()

        return Response(data=StatsSerializer(
            {"results": data, "date": {"from_date": aggregator.from_date, "to_date": aggregator.to_date}}
        ).data)

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
