from django.contrib.auth.decorators import login_required

from django.shortcuts import render

from .carrinho import Carrinho

def add_carrinho(request, produto_id):
    carrinho = Carrinho(request)
    carrinho.add(produto_id)
    
    return render(request, 'carrinho/add_carrinho.html')


def carrinho(request):
    return render(request, 'carrinho/carrinho.html')

@login_required
def checkout(request):
    return render(request, 'carrinho/checkout.html')
