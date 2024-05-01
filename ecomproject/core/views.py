from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.db.models import Q

from django.shortcuts import render, redirect
from produtos.models import Produto, Categoria
from .forms import CadastroForm


#Home
def principal(request):
    produtos = Produto.objects.all()[0:8] #basicly it's gonna show only '8' getting from the database.
    return render(request, 'core/principal.html', {'produtos':produtos})

# Cadastro
def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)

        if form.is_valid():
            usuario = form.save()

            login(request, usuario)

            return redirect('/login/')
    else:
        form = CadastroForm()

    return render(request, 'core/cadastro.html', {
        'form': form
    })

#Logout
def custom_logout(request):
    logout(request)

    return redirect('/')

@login_required
def minhaconta(request):
    return render(request, 'core/minhaconta.html')

#Movéis
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

