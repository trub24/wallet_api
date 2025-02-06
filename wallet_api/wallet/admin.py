from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Wallet, WalletOperations


admin.site.unregister(Group)
admin.site.register(Wallet)
admin.site.register(WalletOperations)
