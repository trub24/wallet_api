import pytest
from http import HTTPStatus


@pytest.mark.django_db
class TestWalletAPI:
    WALLET_URL = '/api/v1/wallet/'
    WALLET_DETAIL_URL = '/api/v1/wallet/{wallet_id}/'
    WALLET_OPERATION_URL = '/api/v1/wallet/{wallet_id}/operation/'

    def test_wallet(self, api_client):
        response = api_client.get(self.WALLET_URL)
        assert response.status_code == HTTPStatus.OK

    def test_wallet_det(self, api_client, wallet):
        response = api_client.get(
            self.WALLET_DETAIL_URL.format(wallet_id=wallet.id)
        )
        assert response.status_code == HTTPStatus.OK

    def test_wallet_op(self, api_client, wallet):
        response = api_client.get(
            self.WALLET_OPERATION_URL.format(wallet_id=wallet.id)
        )
        assert response.status_code == HTTPStatus.OK

    def test_wallet_op_create(self, api_client, wallet):
        data = {'operation': 'DEPOSIT', 'amout': 100.0}
        response = api_client.post(
            self.WALLET_OPERATION_URL.format(wallet_id=wallet.id),
            data=data
        )
        assert response.status_code == HTTPStatus.CREATED
        wallet.refresh_from_db()
        assert wallet.balance == 200.0
