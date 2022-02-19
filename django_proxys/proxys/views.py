from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from .models import Proxy
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class ProxyList(ListView):
    model = Proxy
    paginate_by = 25


class ProxyCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('proxys:entrar')
    model = Proxy
    fields = ['ip_address', 'port', 'protocol', 'anonymity',
              'country', 'region', 'city', 'uptime', 'response', 'transfer']
    success_url = reverse_lazy('proxys:index')


class ProxyUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('proxys:entrar')
    model = Proxy
    fields = ['ip_address', 'port', 'protocol', 'anonymity',
              'country', 'region', 'city', 'uptime', 'response', 'transfer']
    success_url = reverse_lazy('proxys:index')
    template_name = "proxys/proxy_form_edit.html"


class ProxyDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('proxys:entrar')
    model = Proxy
    success_url = reverse_lazy('proxys:index')
