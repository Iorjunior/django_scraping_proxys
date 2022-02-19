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
    uptime = models.IntegerField()
    response = models.IntegerField()
    transfer = models.IntegerField()

    def __str__(self):
        return self.ip_address
