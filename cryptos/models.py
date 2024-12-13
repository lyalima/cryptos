from django.db import models


class Crypto(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    symbol = models.CharField(max_length=5, null=True)
    price = models.FloatField(null=True)
    moment = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} | {self.symbol} | {self.price}'
