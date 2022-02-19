from django.urls import path
from .views import ProxyCreate, ProxyUpdate, ProxyDelete, ProxyList
from django.contrib.auth import views as auth_views

app_name = "proxys"

urlpatterns = [
    path('', ProxyList.as_view(), name='index'),
    path('proxys/cadastrar/', ProxyCreate.as_view(), name='cadastrar-proxy'),
    path('proxys/editar/<int:pk>/', ProxyUpdate.as_view(), name='editar-proxy'),
    path('proxys/deletar/<int:pk>/', ProxyDelete.as_view(), name='deletar-proxy'),
    path('sair/', auth_views.LogoutView.as_view(), name='sair'),
    path('entrar/', auth_views.LoginView.as_view(
        template_name="proxys/login.html"
    ), name='entrar')
]
