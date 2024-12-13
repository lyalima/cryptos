import requests
from celery import shared_task
from .models import Crypto


@shared_task
def get_price_crypto(chain, address):
    url = f'https://coins.llama.fi/prices/current/{chain}:{address},coingecko:{chain}'

    response = requests.get(url)
    data = response.json()

    price = data['coins'][f'coingecko:{chain}']['price']
    symbol = data['coins'][f'coingecko:{chain}']['symbol']

    Crypto.objects.create(
        name=chain,
        symbol=symbol,
        price=price,
    )

    return price, symbol
