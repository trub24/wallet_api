# Generated by Django 3.2.16 on 2025-02-05 12:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Номер кошелька')),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=19, verbose_name='Баланс')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wallet', to=settings.AUTH_USER_MODEL, verbose_name='юзер')),
            ],
            options={
                'verbose_name': 'кошелек',
                'verbose_name_plural': 'Кошельки',
                'default_related_name': 'wallet',
            },
        ),
        migrations.CreateModel(
            name='WalletOperations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amout', models.DecimalField(decimal_places=2, default=0, max_digits=19, verbose_name='Сумма')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('operation', models.CharField(choices=[('DEPOSIT', 'Deposit'), ('WITHDRAW', 'Withdraw')], max_length=256, verbose_name='операция')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='operation', to=settings.AUTH_USER_MODEL, verbose_name='юзер')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='operation', to='wallet.wallet', verbose_name='кошелек')),
            ],
            options={
                'verbose_name': 'операция',
                'verbose_name_plural': 'Операции',
                'ordering': ('-pub_date',),
                'default_related_name': 'operation',
            },
        ),
    ]
