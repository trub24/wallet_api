import pytest
import uuid
from rest_framework.test import APIClient
from wallet.models import Wallet


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def wallet():
    return Wallet.objects.create(
        id=uuid.uuid4(),
        balance=100.0
    )
