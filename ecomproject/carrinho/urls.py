from django.urls import path

from .views import *

urlpatterns = [
    path('carrinho-compras/', carrinho, name='carrinho'),
    path('checkout/', checkout, name='checkout'),
    path('menu_carrinho/<int:produto_id>/', add_carrinho, name='add_carrinho'),
]