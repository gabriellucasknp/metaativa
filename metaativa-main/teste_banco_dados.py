#!/usr/bin/env python
"""
Script de teste para demonstrar o funcionamento do METAATIVA com Django + SQLite
Execute com: python teste_banco_dados.py
"""

import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'metaativa_projeto.settings')
django.setup()

from django.contrib.auth.models import User
from app_metaativa.models import Comunidade, Perfil

def limpar_dados():
    """Limpar dados de teste anteriores"""
    print("🗑️  Limpando dados anteriores...")
    Comunidade.objects.filter(nome__contains='Teste').delete()
    User.objects.filter(username__startswith='usuario_').delete()

def criar_usuarios():
    """Criar usuários de teste"""
    print("\n👥 Criando usuários de teste...")
    
    usuarios_dados = [
        ('usuario_joao', 'joao@teste.com', 'senha123', 28, 'Corrida, Yoga', 'Perder peso'),
        ('usuario_maria', 'maria@teste.com', 'senha456', 32, 'Natação', 'Melhorar resistência'),
        ('usuario_pedro', 'pedro@teste.com', 'senha789', 25, 'Futebol, Ciclismo', 'Ficar mais forte'),
    ]
    
    usuarios = []
    for username, email, password, idade, atividades, objetivo in usuarios_dados:
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username, email, password)
            perfil = Perfil.objects.create(
                user=user,
                idade=idade,
                atividades=atividades,
                objetivo=objetivo
            )
            usuarios.append(user)
            print(f"  ✓ Usuário '{username}' criado com perfil")
        else:
            usuarios.append(User.objects.get(username=username))
            print(f"  ℹ️  Usuário '{username}' já existe")
    
    return usuarios

def criar_comunidades(usuarios):
    """Criar comunidades de teste"""
    print("\n🏃 Criando comunidades de teste...")
    
    comunidades_dados = [
        {
            'nome': 'Teste - Corrida Matinal',
            'esporte': 'corrida',
            'local': 'Parque Central',
            'dias': 'seg,qua,sex',
            'horario': '06:30',
            'descricao': 'Grupo de corrida leve para iniciantes e intermediários'
        },
        {
            'nome': 'Teste - Yoga Relaxante',
            'esporte': 'yoga',
            'local': 'Estúdio Zen',
            'dias': 'ter,qui',
            'horario': '18:00',
            'descricao': 'Aulas de yoga para relaxamento e flexibilidade'
        },
        {
            'nome': 'Teste - Futebol Amador',
            'esporte': 'futebol',
            'local': 'Campo da Vila',
            'dias': 'sab',
            'horario': '14:00',
            'descricao': 'Partidas de futebol entre amigos'
        },
    ]
    
    comunidades = []
    for i, dados in enumerate(comunidades_dados):
        criador = usuarios[i % len(usuarios)]
        
        com = Comunidade.objects.create(
            criador=criador,
            **dados
        )
        comunidades.append(com)
        print(f"  ✓ Comunidade '{com.nome}' criada por {criador.username}")
    
    return comunidades

def adicionar_membros(comunidades, usuarios):
    """Adicionar membros às comunidades"""
    print("\n📍 Adicionando membros às comunidades...")
    
    for com in comunidades:
        # Adicionar 2 membros aleatórios (exceto o criador)
        for usuario in usuarios:
            if usuario != com.criador and usuario not in com.membros.all():
                com.membros.add(usuario)
                print(f"  ✓ {usuario.username} adicionado a '{com.nome}'")

def exibir_resumo(comunidades):
    """Exibir resumo dos dados"""
    print("\n📊 RESUMO DO BANCO DE DADOS")
    print("=" * 60)
    
    print(f"\n👥 Total de usuários: {User.objects.count()}")
    for user in User.objects.all():
        perfil = Perfil.objects.filter(user=user).first()
        if perfil:
            print(f"  • {user.username} ({user.email}) - Idade: {perfil.idade}")
    
    print(f"\n🏃 Total de comunidades: {Comunidade.objects.count()}")
    for com in Comunidade.objects.all():
        print(f"\n  📌 {com.nome}")
        print(f"     Esporte: {com.get_esporte_display()}")
        print(f"     Local: {com.local}")
        print(f"     Horário: {com.horario}")
        print(f"     Dias: {com.dias}")
        print(f"     Criador: {com.criador.username}")
        print(f"     Total de membros: {com.total_membros()}")
        if com.membros.count() > 0:
            membros = ', '.join([m.username for m in com.membros.all()])
            print(f"     Membros: {membros}")

def verificar_banco_de_dados():
    """Verificar informações do banco de dados"""
    print("\n🗄️  INFORMAÇÕES DO BANCO DE DADOS")
    print("=" * 60)
    
    import os
    from django.conf import settings
    
    db_path = settings.DATABASES['default']['NAME']
    if os.path.exists(db_path):
        size_mb = os.path.getsize(db_path) / (1024 * 1024)
        print(f"✓ Banco de dados: {db_path}")
        print(f"  Tamanho: {size_mb:.2f} MB")
    else:
        print(f"✗ Banco de dados não encontrado: {db_path}")

def main():
    """Executar todos os testes"""
    print("\n" + "=" * 60)
    print("🎯 TESTE DO METAATIVA COM DJANGO + SQLite")
    print("=" * 60)
    
    # Verificar banco de dados
    verificar_banco_de_dados()
    
    # Limpar dados anteriores
    limpar_dados()
    
    # Criar dados
    usuarios = criar_usuarios()
    comunidades = criar_comunidades(usuarios)
    adicionar_membros(comunidades, usuarios)
    
    # Exibir resumo
    exibir_resumo(comunidades)
    
    print("\n" + "=" * 60)
    print("✅ TESTE CONCLUÍDO COM SUCESSO!")
    print("=" * 60)
    print("\nPróximos passos:")
    print("1. Execute: python manage.py runserver")
    print("2. Acesse: http://127.0.0.1:8000/")
    print("3. Admin: http://127.0.0.1:8000/admin/ (admin/admin123)")
    print("=" * 60 + "\n")

if __name__ == '__main__':
    main()
