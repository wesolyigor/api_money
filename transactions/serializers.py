from rest_framework import serializers

from transactions.models import Transaction, Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'id',
            'name',
            'description',
            'initial_balance',
        )

class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = (
            'id',
            'amount',
            'description',
            'transaction_type',
            'account',
        )