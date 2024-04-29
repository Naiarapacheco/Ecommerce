from django.contrib import admin
from django.urls import path

from carrinho.views import menu_carrinho
from core.views import principal, moveis
from produtos.views import produto

urlpatterns = [
    path('', principal, name='principal'),
    path('moveis/', moveis, name='moveis'),
    path('produto/<slug:slug>/', produto, name='produto'),
    path('menu_carrinho/<int:produto_id>/', menu_carrinho, name='menu_carrinho'),
    path('admin/', admin.site.urls),
]
