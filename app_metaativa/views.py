from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Perfil, Comunidade
from .forms import CadastroUsuarioForm, EditarPerfilForm, CriarComunidadeForm


def cadastro(request):
    """View para cadastro de novo usuário"""
    if request.method == 'POST':
        form = CadastroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Criar perfil automaticamente
            Perfil.objects.create(user=user)
            messages.success(request, 'Cadastro realizado com sucesso! Faça login.')
            return redirect('login')
    else:
        form = CadastroUsuarioForm()
    return render(request, 'app_metaativa/cadastro.html', {'form': form})


def login_view(request):
    """View para login do usuário"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Bem-vindo, {user.username}!')
            return redirect('menu_principal')
        else:
            messages.error(request, 'Usuário ou senha incorretos.')
    
    return render(request, 'app_metaativa/login.html')


@login_required
def menu_principal(request):
    """View do menu principal após login"""
    comunidades = Comunidade.objects.filter(ativa=True)
    return render(request, 'app_metaativa/menu_principal.html', {
        'comunidades': comunidades
    })


@login_required
def editar_perfil(request):
    """View para editar perfil do usuário"""
    perfil = Perfil.objects.get(user=request.user)
    
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil atualizado com sucesso!')
            return redirect('menu_principal')
    else:
        form = EditarPerfilForm(instance=perfil)
    
    return render(request, 'app_metaativa/editar_perfil.html', {'form': form})


@login_required
def criar_comunidade(request):
    """View para criar nova comunidade"""
    if request.method == 'POST':
        form = CriarComunidadeForm(request.POST)
        if form.is_valid():
            comunidade = form.save(commit=False)
            comunidade.criador = request.user
            comunidade.save()
            messages.success(request, 'Comunidade criada com sucesso!')
            return redirect('menu_principal')
    else:
        form = CriarComunidadeForm()
    
    return render(request, 'app_metaativa/criar_comunidade.html', {'form': form})


@login_required
def visualizar_comunidades(request):
    """View para visualizar todas as comunidades"""
    comunidades = Comunidade.objects.filter(ativa=True)
    return render(request, 'app_metaativa/visualizar_comunidades.html', {
        'comunidades': comunidades
    })


@login_required
def detalhes_comunidade(request, pk):
    """View para ver detalhes de uma comunidade específica"""
    comunidade = get_object_or_404(Comunidade, pk=pk)
    
    if request.method == 'POST':
        if request.POST.get('action') == 'entrar':
            if request.user not in comunidade.membros.all() and request.user != comunidade.criador:
                comunidade.membros.add(request.user)
                messages.success(request, f'Você entrou em {comunidade.nome}!')
            else:
                messages.info(request, 'Você já é membro desta comunidade.')
        elif request.POST.get('action') == 'sair':
            if request.user in comunidade.membros.all():
                comunidade.membros.remove(request.user)
                messages.success(request, f'Você saiu de {comunidade.nome}.')
    
    return render(request, 'app_metaativa/detalhes_comunidade.html', {
        'comunidade': comunidade
    })


@login_required
def logout_view(request):
    """View para logout do usuário"""
    logout(request)
    messages.success(request, 'Você saiu da plataforma.')
    return redirect('login')
