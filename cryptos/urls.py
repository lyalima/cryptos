from django.urls import path
from .views import CryptoPriceView


urlpatterns = [
    path('cryptos/', CryptoPriceView.as_view(), name='crypto-price-view'),
]
