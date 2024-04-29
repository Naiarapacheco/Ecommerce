from django.shortcuts import render

from .carrinho import Carrinho


def menu_carrinho(request, produto_id):
    cart = Carrinho(request)
    cart.add(produto_id)

    return render(request, 'includes/menu_carrinho.html')