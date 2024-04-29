from django.shortcuts import render

from .carrinho import Carrinho


def add_carrinho(request, produto_id):
    cart = Carrinho(request)
    cart.add(produto_id)

    return render(request, 'includes/add_carrinho.html')


def carrinho(request):
    return render(request, 'carrinho/carrinho.html')


def checkout(request):
    return render(request, 'carrinho/checkout.html')
