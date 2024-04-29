from django.db.models import Q

from django.shortcuts import render

from produtos.models import Produto, Categoria


def principal(request):
    produtos = Produto.objects.all()[0:8] #basicly it's gonna show only '8' getting from the database.

    return render(request, 'core/principal.html', {'produtos':produtos})


def cadastro(request):
    return render(request, 'core/cadastro.html')


def login(request):
    return render(request, 'core/login.html')


def moveis(request):
    categorias = Categoria.objects.all()
    produtos = Produto.objects.all() 

    active_categoria = request.GET.get('categoria', '')

    if active_categoria:
        produtos = produtos.filter(categoria__slug=active_categoria)

    query = request.GET.get('query', '')

    if query:
        produtos = produtos.filter(Q(nome__icontains=query) | Q(descricao__icontains=query))

    contexto = {
        'categorias': categorias,
        'produtos': produtos,
        'active_categoria': active_categoria
    }
    return render(request, 'core/moveis.html', contexto)

