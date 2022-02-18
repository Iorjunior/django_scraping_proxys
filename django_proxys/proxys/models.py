from urllib import response
from django.db import models


class Proxy(models.Model):
    ip_address = models.CharField(max_length=15)
    port = models.CharField(max_length=5)
    protocol = models.CharField(max_length=5)
    anonymity = models.CharField(default='None', max_length=4)
    country = models.CharField(max_length=56)
    region = models.CharField(max_length=56)
    city = models.CharField(max_length=56)
    uptime = models.DecimalField(decimal_places=2, max_digits=4)
    response = models.IntegerField()
    transfer = models.IntegerField()
