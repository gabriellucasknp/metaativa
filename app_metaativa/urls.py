from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_principal, name='menu_principal'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('comunidade/criar/', views.criar_comunidade, name='criar_comunidade'),
    path('comunidades/', views.visualizar_comunidades, name='visualizar_comunidades'),
    path('comunidade/<int:pk>/', views.detalhes_comunidade, name='detalhes_comunidade'),
]
