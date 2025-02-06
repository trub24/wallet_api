from django.db import transaction
from rest_framework import serializers
from wallet.models import Wallet, WalletOperations


class WalletSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wallet
        fields = (
            'id',
            'balance',
        )


class WalletOperationsSerializer(serializers.ModelSerializer):
    amout = serializers.DecimalField(
        max_digits=19,
        decimal_places=2
    )
    wallet = WalletSerializer(read_only=True)
    operation = serializers.ChoiceField(
        choices=WalletOperations.Operations.choices
    )

    class Meta():
        model = WalletOperations
        fields = (
            'wallet',
            'amout',
            'pub_date',
            'operation'
        )
        read_only_fields = ('pub_date',)

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                'Количество не может быть меньше нуля'
            )
        return value

    def validate_wallet(self, value):
        if Wallet.objects.filter(id=value).exists():
            return value
        raise serializers.ValidationError('Кошелек отсутствет')

    def create(self, validated_data):
        wallet_uuid = self.context['view'].kwargs.get('wallet_id')
        try:
            with transaction.atomic():
                wallet = Wallet.objects.select_for_update().get(id=wallet_uuid)
                print(wallet.balance)
                amout = validated_data.pop('amout')
                operation_type = validated_data.pop('operation')
                if operation_type == 'WITHDRAW' and wallet.balance < amout:
                    raise serializers.ValidationError(
                        'Количество не может быть больше баланса'
                    )
                elif operation_type == 'WITHDRAW':
                    wallet.balance -= amout
                elif operation_type == 'DEPOSIT':
                    wallet.balance += amout
                else:
                    raise serializers.ValidationError(
                        'Не верный тип операции'
                    )
                wallet.save()
                operation = WalletOperations.objects.create(
                    amout=amout,
                    wallet=wallet,
                    operation=operation_type,
                )
                operation.save()
                return operation
        except Wallet.DoesNotExist:
            raise serializers.ValidationError('Кошелек отсутствет')
