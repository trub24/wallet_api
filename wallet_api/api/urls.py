from django.urls import include, path
from rest_framework import routers
from .views import WalletViewSet, WalletOperationsViewSet


name = 'api'

router = routers.DefaultRouter()

router.register(r'wallet', WalletViewSet, basename='wallet')
router.register(
    r'wallet/(?P<wallet_id>[^/.]+)/operation',
    WalletOperationsViewSet,
    basename='operation'
)


urlpatterns = [
    path('v1/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
