from django.contrib import admin
from proxys.models import Proxy


@admin.register(Proxy)
class Proxys(admin.ModelAdmin):
    list_display = ("ip_address", "port", "protocol", "country", "uptime")
    search_fields = ['country']
