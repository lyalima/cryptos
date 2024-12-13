from rest_framework import views, status, response
from .serializers import CryptoModelSerializer
from .models import Crypto
from .tasks import get_price_crypto


class CryptoPriceView(views.APIView):

    def post(self, request):
        crypto_chain = request.data.get('crypto_chain')
        crypto_address = request.data.get('crypto_address')

        get_price_crypto.delay(crypto_chain, crypto_address)

        return response.Response(
            data={'message': 'Tarefa disparada com sucesso.'},
            status=status.HTTP_200_OK,
        )
    
    def get(self, request):
        cryptos = Crypto.objects.all()

        return response.Response(
            data=CryptoModelSerializer(cryptos, many=True).data,
            status=status.HTTP_200_OK,
        ) 
