from .carrinho import Carrinho


#available everywhere
def carrinho(request):
    return {'cart': Carrinho(request)}