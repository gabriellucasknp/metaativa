METAATIVA — Apresentação
🚦 Visão Geral
Stack: Django 4, Python 3.13, SQLite (dev), HTML/CSS puro.
Problema: organizar comunidades esportivas com cadastro, login, perfis e grupos.
Solução: web app com autenticação, CRUD de comunidades e relacionamento muitos-para-muitos entre usuários e comunidades.
🧭 Passo a Passo de Construção (storytelling)
Ambiente — criei uma venv e instalei dependências.
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
Projeto Django — configurei settings.py com SQLite, INSTALLED_APPS e templates. A raiz do projeto está em metaativa_projeto/.

Aplicação — criei app_metaativa/ para concentrar domínio e UI.

Modelagem

Perfil: extensão do User (OneToOne) com idade, atividades e objetivo.
Comunidade: nome, esporte (choices), local, dias, horário, criador (FK User), membros (ManyToMany User), ativa.
Forms e Views — formulários para cadastro de usuário, edição de perfil e criação de comunidade; views protegidas com login_required para CRUD básico e entrada/saída de comunidades.

Templates — base HTML + páginas de login, cadastro, menu principal, criar/editar perfil e comunidades. CSS simples embutido para demonstrar.

Migrations & Dados — rodei migrations e criei um superusuário. O banco db.sqlite3 foi removido do repositório; você gera o seu rodando migrate.

▶️ Como Rodar (5 minutos)
cd metaativa-main
.\.venv\Scripts\activate          # ative sua venv
pip install -r requirements.txt     # garanta dependências
python manage.py migrate            # cria o SQLite local
python manage.py createsuperuser    # crie seu admin
python manage.py runserver          # suba em http://127.0.0.1:8000/
URLs principais:

Home: http://127.0.0.1:8000/
Admin: http://127.0.0.1:8000/admin/
🗂️ Estrutura Essencial
metaativa-main/
├── manage.py
├── requirements.txt
├── metaativa_projeto/        # settings, urls, wsgi
├── app_metaativa/            # domínio e views
│   ├── models.py             # Perfil, Comunidade
│   ├── forms.py              # Cadastro, Perfil, Comunidade
│   ├── views.py              # Fluxos autenticados
│   ├── urls.py               # Rotas da app
│   └── admin.py              # Admin Django
└── templates/app_metaativa/  # HTML/CSS das telas
🔍 O que mostrar numa entrevista
Modelagem: Perfil estende User; Comunidade usa FK (criador) + M2M (membros). Choices para esportes e dias garantem consistência.
Segurança: autenticação Django, senhas com hash, CSRF nos forms, login_required nas views sensíveis.
Camadas: forms.py valida entrada; views.py coordena fluxo; templates/ renderiza; admin.py dá painel de gestão pronto.
Escalabilidade: fácil migrar SQLite → Postgres mudando DATABASES em settings.py; migrações versionadas.
DX: scripts simples, dependências mínimas, CSS no template para evitar setup adicional.
🧪 Teste Rápido Automatizado
Há um script de seed/teste que popula dados fictícios:

python manage.py migrate
python teste_banco_dados.py
Ele cria usuários/comunidades de demonstração e imprime um resumo no console.

📌 Comandos Úteis
python manage.py makemigrations app_metaativa
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
python manage.py test
🧹 O que foi limpo
Removi arquivos redundantes de resumo e o db.sqlite3 gerado, para manter o repo enxuto. Gere seu banco local com migrate.
🚀 Próximos Passos
Migrar para Postgres para produção.
Adicionar upload de fotos e notificações.
Expor API REST (Django REST Framework) para mobile.
Adicionar testes de integração para fluxos de comunidade.
