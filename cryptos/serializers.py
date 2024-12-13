from rest_framework import serializers
from .models import Crypto


class CryptoModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Crypto
        fields = '__all__'
