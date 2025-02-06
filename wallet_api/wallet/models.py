import uuid
from django.db import models


class Wallet(models.Model):
    id = models.UUIDField(
        'Номер кошелька',
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    balance = models.DecimalField(
        'Баланс',
        max_digits=19,
        decimal_places=2,
        default=0
    )

    class Meta:
        default_related_name = 'wallet'
        verbose_name = 'кошелек'
        verbose_name_plural = 'Кошельки'


class WalletOperations(models.Model):
    class Operations(models.TextChoices):
        DEPOSIT = 'DEPOSIT'
        WITHDRAW = 'WITHDRAW'

    wallet = models.ForeignKey(
        Wallet,
        on_delete=models.CASCADE,
        verbose_name='кошелек'
    )
    amout = models.DecimalField(
        'Сумма',
        max_digits=19,
        decimal_places=2,
        default=0
    )
    pub_date = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True
    )
    operation = models.CharField(
        'операция',
        max_length=256,
        choices=Operations.choices
    )

    class Meta:
        ordering = ('-pub_date', )
        default_related_name = 'operation'
        verbose_name = 'операция'
        verbose_name_plural = 'Операции'

    def __str__(self):
        return f'{self.operation}, {self.amout}, {self.wallet}'
