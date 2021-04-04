from transactions.models import Account, Transaction


class AccountAggregator:

    def __init__(self, from_date, to_date):
        self.to_date = to_date
        self.from_date = from_date

        filters = {}
        if self.from_date:
            filters["created__gte"] = self.from_date

        if self.to_date:
            filters["created__lte"] = self.to_date

        self.transaction_qs = Transaction.objects.filter(**filters)

    def aggregate_data(self):
        data = []

        for account in Account.objects.all():
            data.append(
                {"id": account.id,
                 "name": account.name,
                 'amount_in': account.amount_in(transaction_qs=self.transaction_qs),
                 'amount_out': account.amount_out(transaction_qs=self.transaction_qs),
                 'balance': account.balance(transaction_qs=self.transaction_qs),
                 }
            )
        return data