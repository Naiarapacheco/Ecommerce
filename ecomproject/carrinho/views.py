from django.shortcuts import render

from .carrinho import Carrinho


def menu_carrinho(request, produto_id):
    cart = Carrinho(request)
    cart.add(produto_id)

    return render(request, 'includes/menu_carrinho.html')


def carrinho_compras(request):
    return render(request, 'carrinho/carrinho_compras.html')


def checkout(request):
    return render(request, 'carrinho/checkout.html')
