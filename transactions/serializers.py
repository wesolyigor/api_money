from rest_framework import serializers

from transactions.constans import TransactionTypE
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
    transaction_type_display = serializers.SerializerMethodField()

    class Meta:
        model = Transaction
        fields = (
            'id',
            'amount',
            'description',
            'transaction_type',
            'account',
            'transaction_type_display',
            'created',
        )

    def get_transaction_type_display(self, obj):
        return TransactionTypE(obj.transaction_type).name


class StatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'id',
            'name',
            'amount_in',
            'amount_out',
            'balance',
        )


class StatsFilterSerializer(serializers.Serializer):
    from_date = serializers.DateField(required=True)
    to_date = serializers.DateField(required=True)
