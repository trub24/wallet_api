from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin
)
from wallet.models import Wallet
from .serializers import (
    WalletSerializer, WalletOperationsSerializer
)


class WalletViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = WalletSerializer
    lookup_field = 'id'

    def get_queryset(self):
        queryset = Wallet.objects.all()
        return queryset


class WalletOperationsViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = WalletOperationsSerializer

    def get_wallet_obj(self):
        return get_object_or_404(Wallet, id=self.kwargs.get('wallet_id'))

    def get_queryset(self):
        queryset = self.get_wallet_obj().operation.all()
        return queryset

    def perform_create(self, serializer):
        serializer.save(wallet=self.get_wallet_obj())
