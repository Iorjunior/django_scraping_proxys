from django.contrib import admin
from proxys.models import Proxy


class Proxys(admin.ModelAdmin):
    list_diplay = ('ip_address', 'port', 'protocol', 'country', 'uptime')


admin.site.register(Proxy, Proxys)
