from django.contrib import admin
from .models import Perfil, Comunidade


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'idade', 'atividades', 'data_criacao')
    search_fields = ('user__username', 'atividades')
    readonly_fields = ('data_criacao', 'data_atualizacao')


@admin.register(Comunidade)
class ComunidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'esporte', 'local', 'criador', 'total_membros', 'ativa')
    search_fields = ('nome', 'esporte', 'local')
    filter_horizontal = ('membros',)
    readonly_fields = ('data_criacao',)
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'descricao', 'esporte', 'local')
        }),
        ('Horário e Dias', {
            'fields': ('dias', 'horario')
        }),
        ('Membros', {
            'fields': ('criador', 'membros')
        }),
        ('Status', {
            'fields': ('ativa', 'data_criacao')
        }),
    )
